import { useEffect, useState, useRef } from 'react'
import './App.css'
import './TerminalEffect.css'

interface Card {
  question: string;
  answer: string;
}

function useFlashcards(cards: Card[]) {
  const [output, setOutput] = useState<string[]>([]);
  const [prompt, setPrompt] = useState<string>("");
  const [done, setDone] = useState<boolean>(false);
  const [currentIndex, setCurrentIndex] = useState<number>(0);

  const start = () => {
    setOutput(["Welcome! Type 'start' to begin flashcards, or 'help' for commands."]);
    setPrompt("Ready");
  };

  const sendInput = (input: string) => {
    const cmd = input.trim().toLowerCase();
    
    if (cmd === 'start') {
      setCurrentIndex(0);
      setPrompt(cards[0]?.question || "No cards available");
      setOutput((prev: string[]) => [...prev, `> ${input}`, "Starting flashcards..."]);
    } else if (cmd === 'help') {
      setOutput((prev: string[]) => [...prev, `> ${input}`, "Commands: start, next, quit"]);
    } else if (cmd === 'next') {
      const nextIndex = currentIndex + 1;
      if (nextIndex < cards.length) {
        setCurrentIndex(nextIndex);
        setPrompt(cards[nextIndex].question);
        setOutput((prev: string[]) => [...prev, `> ${input}`, `Moving to question ${nextIndex + 1}...`]);
      } else {
        setDone(true);
        setPrompt("Complete!");
        setOutput((prev: string[]) => [...prev, `> ${input}`, "All cards completed!"]);
      }
    } else if (cmd === 'quit') {
      setDone(true);
      setPrompt("Goodbye");
      setOutput((prev: string[]) => [...prev, `> ${input}`, "Exiting flashcards..."]);
    } else {
      setOutput((prev: string[]) => [...prev, `> ${input}`, `Answer: ${cards[currentIndex]?.answer || 'N/A'}`, "Type 'next' for next card"]);
    }
  };

  return { output, prompt, start, sendInput, done };
}

const sampleCards = [
  { question: "What is the capital of France?", answer: "Paris" },
  { question: "What is 2 + 2?", answer: "4" },
  { question: "What color is the sky?", answer: "Blue" }
];

function App() {
  var styling = localStorage.getItem("styling");
  const [input, setInput] = useState("");
  const { output, prompt, start, sendInput, done } = useFlashcards(sampleCards)
  const inputRef = useRef<HTMLTextAreaElement>(null);
   const terminalEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Focus the input when the component mounts
    start();
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []); // Empty dependency array ensures it runs only once after initial render

  useEffect(() => {
    // Auto-scroll to bottom when output changes
    if (terminalEndRef.current) {
      terminalEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [output]);

  const handleKey = () => {
    if (inputRef.current && document.activeElement !== inputRef.current) {
      inputRef.current.focus();
    }
  }

  // called when the enter key is pressed
  const enterCommand = () => {
    if (input.trim()) {
      sendInput(input);
      setInput("");
    }
  }

   useEffect(() => {
    document.addEventListener("keydown", handleKey);
    return () => {
      document.removeEventListener("keydown", handleKey);
    };
  }, []);

  const text_input = document.getElementById("text-input"); // get reference to the text area

  if(text_input != null) {
    text_input.addEventListener("onblur", () => {
      text_input.focus();
    });
  }

  function changeStyling() {
    if(styling == "old") {
      styling = "new";
    } else {
      styling = "old";
    }
    localStorage.setItem("styling", styling); // save the current styling in the local storage so that it saves when the page is reloaded
    location.reload();
  }
  
  if(styling == "new") {
    return (
      <>
        <h1>Terminal Flashcards</h1>
        <div className="card">
          <button className="to-old-styling" onClick={() => changeStyling()}>
            Switch to oldschool terminal styling
          </button>
        </div>
      </>
    )
  } else {
    return (
      <>
        <div className='terminal-screen refresh'>
          <div> {/* controls what text is non changeable and happens before the user is able to type */}
            [Terminal Flashcards]<br></br>
            Install the executable and view updates at https://github.com/alxroum/terminal_flashcards<br/>
            =========================================================================================<br/>
          </div>

          <div id="appendable-section"> {/* this is where console text will be added */}
            {output.map((line, index) => (
              <div key={index} className="mb-1">
                {line}
              </div>
            ))}
          </div>

          <span id="current-terminal-line">
            os/root/user:~{'$'}{' '}
            <textarea 
              autoFocus
              id='text-area' 
              ref={inputRef}
              rows={1}
              value={input}
              onKeyDown={k=>{
                if(k.key === "Enter") {
                  enterCommand()
                  k.preventDefault(); // prevent the text area from moving to new line when enter is pressed
                }
              }}
              onChange={e=>setInput(e.target.value)}
            />
          </span>
          <div ref={terminalEndRef} />
          {/*<span id='cursor'>{'\u2588'}</span>*/}
        </div>
      </>
    )
  }
}

export default App

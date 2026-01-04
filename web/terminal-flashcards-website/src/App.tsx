import { useEffect, useState, useRef } from 'react'
import './App.css'
import './TerminalEffect.css'

interface Card {
  term: string;
  definition: string;
}

function useFlashcards(cards: Card[]) {
  const [output, setOutput] = useState<string[]>([]);
  const [prompt, setPrompt] = useState<string>("");
  const [done, setDone] = useState<boolean>(false);
  const [currentIndex, setCurrentIndex] = useState<number>(0);

  const start = () => {
    setOutput([""]);
    setPrompt("");
  };

  const sendInput = (input: string) => {
    const _arguments = input.trim().toLowerCase().split(' ');
    console.log(_arguments);
    
    const prev_commands = document.getElementById("previous-commands");
    // make sure the input is valid
    // the enterCommand function already screens for no input, so we at least have something in input
    if(_arguments[0] == 'help') {
      // previous command call is saved to 'previous-commands' div
      if(prev_commands) prev_commands.innerHTML += ">> help";
      setPrompt("") // prompt will be set to the output of the command
    }
    
  };

  return { output, prompt, start, sendInput, done };
}

const sampleCards = [
  { term: "What is the capital of France?", definition: "Paris" },
  { term: "What is 2 + 2?", definition: "4" },
  { term: "What color is the sky?", definition: "Blue" }
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

  const handleKey = (e: Event) => {
    if (inputRef.current && document.activeElement !== inputRef.current) {
      inputRef.current.focus();
      e.preventDefault(); // prevent uncommon error of going to a new line when text area is refocused by pressing enter
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
    document.addEventListener("keydown", e => {handleKey(e)});
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
            Welcome to terminal flashcards! Enter a command to get started, or type 'help' for commands.
          </div>

          <div id="previous-commands"> {/* this is where the previous commands will be added to the screen */}
          
          </div>

          <div>{prompt}</div>

          <div id="current-card"> {/* this is where the currently displayed card will be added */}
            {output}
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

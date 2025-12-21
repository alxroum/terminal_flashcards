import { useEffect, useState, useRef } from 'react'
import './App.css'
import './TerminalEffect.css'

function App() {
  var styling = localStorage.getItem("styling");
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    // Focus the input when the component mounts
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []); // Empty dependency array ensures it runs only once after initial render

  const handleClick = () => {
    // Focus the input programmatically on button click
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }

  // called when the enter key is pressed
  const enterCommand = () => {
    if(inputRef.current) {
      var text = inputRef.current.value;
      console.log(text);
    }
  }

  // adding event listeners
  document.addEventListener("click", handleClick); 

  const text_input = document.getElementById("text-input");
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
          <span> {/* controls what text is non changeable and happens before the user is able to type */}
            [Terminal Flashcards]<br></br>
            Install the executable and view updates at https://github.com/alxroum/terminal_flashcards<br/>
            =========================================================================================<br/>
            os/root/user:~{'$'}{' '}
          </span>

          {/*<span id='cursor'>{'\u2588'}</span>*/}
          <input 
            autoFocus
            id='text-input' 
            ref={inputRef}
            type="text"
            value={input}
            onKeyDown={k=>{
              if(k.key === "Enter") {
                enterCommand()
              }
            }}
            onChange={e=>setInput(e.target.value)}
          />
        </div>
      </>
    )
  }
}

export default App

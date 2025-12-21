import { useState } from 'react'
import tfLogo from './assets/updated_icon.svg'
import { useTypewriter, Cursor } from 'react-simple-typewriter'
import './App.css'
import './TerminalEffect.css'

function App() {
  var styling = localStorage.getItem("styling");

  function type_chars() {
    var chars = document.getElementById("text-input")?.innerHTML;
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
            Terminal Flashcards<br></br>

            Install the executable and view updates at https://github.com/alxroum/terminal_flashcards<br></br>

            PS F:\Files\Code Projects and Other Stuff\Github\terminal_flashcards{'\u003E'}
          </span>

          <span id='cursor'>{'\u2588'}</span>
          <span className="terminal-input-region"> {/* controls the region that the user is able to type */}
            <input id='text-input' onChange={type_chars}>
              
            </input>
          </span>
        </div>
      </>
    )
  }
}

export default App

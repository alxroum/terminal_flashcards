import { useState, useRef } from "react";
import { createFlashcardEngine } from "./flashcardEngine";

export function useFlashcards(data) {
  const engineRef = useRef(null);

  const [output, setOutput] = useState("");
  const [prompt, setPrompt] = useState("");
  const [done, setDone] = useState(false);

  function start() {
    engineRef.current = createFlashcardEngine(data);
    const result = engineRef.current.start();
    setOutput(result.output);
    setPrompt(result.prompt);
  }

  function sendInput(input) {
    if (!engineRef.current || done) return;

    const result = engineRef.current.handleInput(input);

    if (result?.quit) {
      setDone(true);
      setPrompt("Session ended.");
      return;
    }

    setOutput(result.output);
    setPrompt(result.prompt);
  }

  return {
    output,
    prompt,
    start,
    sendInput,
    done
  };
}
import { displayCard } from "./displayCard";

export function createFlashcardEngine(data) {
  const keys = Object.keys(data);

  let idx = 0;
  let defaultSide = 0; // 0 = term, 1 = definition
  let currentSide = defaultSide;

  function normalizeIndex() {
    if (idx >= keys.length) idx = 0;
    if (idx < 0) idx = keys.length - 1;
  }

  function getCardText() {
    const key = keys[idx];
    return currentSide === 0 ? key : data[key];
  }

  function getDisplay() {
    return displayCard(getCardText());
  }

  function handleInput(input) {
    switch (input) {
      case "f":
        currentSide = 1 - currentSide;
        break;

      case "b":
        idx--;
        currentSide = defaultSide;
        break;

      case "t":
        defaultSide = 1 - defaultSide;
        currentSide = defaultSide;
        break;

      case "":
        idx++;
        currentSide = defaultSide;
        break;

      case "q":
        return { quit: true };

      default:
        break;
    }

    normalizeIndex();

    return {
      output: getDisplay(),
      prompt:
        "next (enter), flip (f), back (b), toggle default (t), quit (q)"
    };
  }

  return {
    start() {
      return {
        output: getDisplay(),
        prompt:
          "next (enter), flip (f), back (b), toggle default (t), quit (q)"
      };
    },
    handleInput
  };
}
function displayCard(text, width = 52, padding = 2) {
  const innerWidth = width - padding * 2;
  const lines = [];

  lines.push("+" + "-".repeat(width) + "+");

  const wrapped = text.match(new RegExp(`.{1,${innerWidth}}`, "g")) || [""];
  wrapped.forEach(line => {
    lines.push(
      "|" +
      " ".repeat(padding) +
      line.padEnd(innerWidth) +
      " ".repeat(padding) +
      "|"
    );
  });

  lines.push("+" + "-".repeat(width) + "+");

  return lines.join("\n");
}

module.exports = { displayCard };
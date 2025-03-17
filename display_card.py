import math


# this finction will display a terminal text representation of a flashcard. The card will always be maxWidth
# characters wide
def display_card(str, maxWidth, padding):
    
    cardLines = []
    output = ""

    widthPad = padding  # how much space between text and the border

    maxTextPerLine = maxWidth - (2 * widthPad) - 2  # max space allowed for text to achieve the correct width

    words = str.split(' ')  # each word in the string
    lengths = [len(i) for i in words]  # lengths of each word
    totalLen = len(str)  # length of the full string

    textLines = []
    start = 0
    count = 0  # count how many characters we have handled

    while start + maxTextPerLine < totalLen:

        curr = str[start:start + maxTextPerLine]

        last = start + len(curr)  # index after last of curr
        if last < totalLen and str[last] != ' ':  # if the next character after curr stops isn't a space
            last = start + curr.rfind(' ')  # find first space searching backwards
            curr = str[start:last]

        #ext = curr.lstrip()

        if start == 0:
            textLines.append(curr.lstrip() + " " * (maxTextPerLine - len(curr)))
        else:
            textLines.append(curr.lstrip() + " " * (maxTextPerLine - len(curr) + 1))

        start = last
        count += len(curr)

    ext = 0
    if len(str[start:].lstrip() + " " * (maxTextPerLine - len(str[start:]))) < maxTextPerLine:
       ext = 1

    textLines.append(str[start:].lstrip() + " " * (maxTextPerLine - len(str[start:]) + ext))
    
    cardLines.append("." + "-" * (maxTextPerLine + (2 * widthPad)) + ".")
    
    [cardLines.append("|" + " " * widthPad + i + " " * widthPad + "|") for i in textLines]
    cardLines.append("'" + "-" * (maxTextPerLine + (2 * widthPad)) + "'")

    for i in cardLines:
        output += i + '\n'

    return output  # eventually this will return one string separated by /n


# def main():
#     print("Hello, World!")

#     print(display_card("Term1", 26, 2))

#main()
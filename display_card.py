import math


# this finction will display a terminal text representation of a flashcard. The card will always be maxWidth
# characters wide

# TODO --  change display_card to be a helper function that updates the settings from a display_settings.json file
# this will then call the current function which will display to the terminal, the correct specifications for the flashcard
def display_card(str, maxWidth, paddingx, paddingy):
    
    cardLines = []
    output = ""

    widthPad = paddingx  # how much space between text and the border
    heightPad = paddingy;  # 2 lines of height padding

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
    
    cardLines.append("." + "-" * (maxTextPerLine + (2 * widthPad)) + ".")  # top line

    [cardLines.append("|" + " " * widthPad + " " * maxTextPerLine + " " * widthPad + "|") for x in range(heightPad)]  # height padding
    
    [cardLines.append("|" + " " * widthPad + i + " " * widthPad + "|") for i in textLines]  # text

    [cardLines.append("|" + " " * widthPad + " " * maxTextPerLine + " " * widthPad + "|") for x in range(heightPad)]  # height padding
    
    cardLines.append("'" + "-" * (maxTextPerLine + (2 * widthPad)) + "'")  # bottom line

    for i in cardLines:
        output += i + '\n'

    return output  # eventually this will return one string separated by /n


# def main():
#     print("Hello, World!")

#     print(display_card("Term1", 26, 2))

#main()
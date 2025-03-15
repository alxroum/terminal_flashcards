import display_card as dc
import sys

cardWidth = 30
cardHeight = 8


class Flashcard:

    def __init__(self, term, definition):
        self.__term = term
        self.__definition = definition

    def get_term(self):
        return self.__term

    def get_def(self):
        return self.__definition

    def set_term(self, term):
        self.__term = term

    def set_def(self, definition):
        self.__definition = definition

    def print_term(self):
        print(self.__term)

    def print_def(self):
        print(self.__definition)

    def print_both(self):
        print(self.__term, " --> ", self.__definition)


class FlashcardSet:

    def __init__(self, cards):
        self.__cards = cards
        self.__size = len(cards)

    @staticmethod
    def import_from_file(file):
        # return a flashcard set from the data in the file
        pass

    def get_size(self):
        return self.__size

    def get_cards(self):
        return self.__cards


def practice_set():
    go = "\n"
    idx = 0

    while go == "n":
        # do something

        go = input("Next Card?")
        idx += 1
    print("Exiting.")
    return


def main():
    _pr_mode = 0
    _cr_mode = 0
    _vw_mode = 0

    print("Hello, World")
    print(sys.argv)

    if len(sys.argv) > 1:

        match sys.argv[1]:

            case "pr":
                print("Practice Mode:")
                _pr_mode = 1

            case "cr":
                print("Create Mode:")
                _cr_mode = 1

            case "vw":
                print("View Mode:")
                _vw_mode = 1

            case _:
                print("Invalid Mode Selected, Entering View Mode.")

    else:
        print("View Mode:")
        _vw_mode = 1

main()
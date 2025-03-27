import display_card as dc
import sys
import json
import os

cardWidth = 30
cardHeight = 8

# https://stackoverflow.com/questions/5458048/how-can-i-make-a-python-script-standalone-executable-to-run-without-any-dependen

#TODO 

# Combine the edit mode and the create mode so that every file modification can be done in one mode. Also implement a way to delete cards from the file

# for delete, makde d delete with an extra prompt to "are you sure you want to delete?"
# if instead, dp is typed, "delete permanently", do not prompt and just delete immediately

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

def clear_screen():  # clears terminal screen
    os.system('cls')

def delete_card(*data, key): # this method will just delete a card from the dictionary and WILL NOT update the file afterwards, save_json will need to be called to save to the file.

    del data[key]

def read_json(file):
    # returns a dictionary of terms and definitions based on the json file
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("File Not Found.")
        exit_program()
    else: return None

def save_json(file, data):
    try:
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)
            return
    except FileNotFoundError:
        print("File Not Found.")
        exit_program()
    else: 
        print("Saved Succesfully.")
        return None

def save_and_exit(file, data):
    
    save_json(file, data)
    exit_program()

def exit_program():  # in case needed this is always the last thing that runs before program exits

    exit()

def practice_mode(filename):

    #set = FlashcardSet()
    data = read_json(filename)
    if(data != None):
        # successfull file reading
        go = ""
        idx = 0
        clear_screen()

        keys = list(data.keys())
        termdef = 0  # 0 for term, 1 for definition

        while go == "":
            # do something
            if(idx > len(keys) - 1):  # loop back to start
                idx = 0

            termdef = 0  # change this to determine if cards start as term or definition

            if(termdef == 0):
                line = keys[idx]
            else:
                line = data[keys[idx]]

            print(dc.display_card(line, 26, 2))

            go = input("next (enter), flip (f), exit (e): ")

            while(go == "f"): 
                # flip card
                clear_screen()
                if(termdef == 0):
                    termdef = 1
                    line = data[keys[idx]]
                else:
                    termdef = 0
                    line = keys[idx]

                print(dc.display_card(line, 26, 2))

                go = input("next (enter), flip (f), exit (e): ")

            if(go == 'e'):
                exit_program()
            elif(go != ""):
                go = ""
            idx += 1  # go to the next card
            clear_screen()
        exit_program()
    
    else:
        print("File Not Found, Exiting.")
        exit_program()

def create_mode(filename):

    data = read_json(filename)
    if(data != None):
        go = "y"

        while(go.lower() == 'y' or go.lower() == 'yes'):
            
            term = input("Enter the new term: ")
            definition = input("Enter the new definition: ")

            data[term] = definition

            go = input("Would you like to create another flashcard? y/n: ")
        
        save_and_exit(filename, data)

def edit_mode(filename):

    #set = FlashcardSet()
    data = read_json(filename)
    if(data != None):
        # successfull file reading
        go = ""
        idx = 0

        keys = list(data.keys())
        termdef = 0  # 0 for term, 1 for definition

        while go == "":
            # do something
            if(idx > len(keys) - 1):  # loop back to start
                idx = 0

            termdef = 0  # this can be set to 1 by default to display the definition first

            if(termdef == 0):
                line = keys[idx]
            else:
                line = data[keys[idx]]

            print(dc.display_card(line, 26, 2))

            go = input("next (enter), flip (f), exit (e): ")

            while(go == "f"): 
                # flip card
                if(termdef == 0):
                    termdef = 1
                    line = data[keys[idx]]
                else:
                    termdef = 0
                    line = keys[idx]

                print(dc.display_card(line, 26, 2))

                go = input("next (enter), flip (f), exit (e): ")

            if(go == 'e'):
                save_and_exit()
            elif(go != ""):
                go = ""
            idx += 1
        exit_program()
    
    else:
        print("File Not Found, Exiting.")
        exit_program()


def main():

    try:
        if(sys.argv[1] == 'help'):
            print("Usage: fcm <mode> <filename>")
            print("Modes: practice (pr), create (cr), edit (em)")
            print("Filename: exclude file extension (file should be a json file)")
            exit()

        if(len(sys.argv) > 2):
            # we have expected arguments

            filename = sys.argv[2] 
            filename += '.json'


            match sys.argv[1]:

                case "pr":
                    print("Practice Mode:")
                    practice_mode(filename)

                case "cr":
                    print("Create Mode:")
                    create_mode(filename)

                case "em":
                    print("Edit Mode")
                    clear_screen()  # testing purposes !!!

                case _:
                    print("Invalid Mode Selected, Entering Practice Mode.")

        else:
            print("Unexpected Arguments. usage: fcm <mode> <filename>")
            exit()
    except Exception:
        print("Error, Invalid Arguments. Exiting.")
    # at this point we have either exited because of error or continued with a mode flag selected

main()
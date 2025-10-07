import display_card as dc
import sys
import json
import os


# TODO

# make a program save file that stores flashcard display settings as well as whether the term or definition is shown first

# add an elimination mode where you can delete cards that you know

cardWidth = 30
cardHeight = 8

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

def find_json(file):
    try:
        with open(file, 'r') as f:
            return True
    except FileNotFoundError:
        return False

def save_json(file, data):
    try:
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)
            return
    except FileNotFoundError:
        print("File Not Found.")
        exit_program()
    finally: 
        print("Saved Succesfully.")
        return None

def save_and_exit(file, data):
    
    save_json(file, data)
    exit_program()

def exit_program():  # in case needed this is always the last thing that runs before program exits

    exit()

def practice_mode(filename):

    data = read_json(filename)
    td_default = 0  # whether the cards show term or definition first, 0 for term, 1 for definition

    if(data != None):
        # successfull file reading
        go = ""
        idx = 0
        clear_screen()

        keys = list(data.keys())
        termdef = td_default  # 0 for term, 1 for definition

        while go == "":  # program should continue

            clear_screen()

            if(idx > len(keys) - 1):  # loop back to start
                idx = 0
            if(idx < 0):
                idx = len(keys) - 1  # loop to end

            line = ''

            if termdef == 0:
                line = keys[idx]
            else:
                line = data[keys[idx]]

            # print the card to the screen by calling the display_card method
            print(dc.display_card(line, 26 * 2, 2, 2))

            if td_default == 0: # display options based on default
                go = input("next (enter), flip (f), back (b), term first (t), quit (q): ")
            else:
                go = input("next (enter), flip (f), back (b), definition first (t), quit (q): ")

            if go == 'q':
                clear_screen()
                exit_program()
            
            elif go == 'f':  # flip term and loop again, without going to the next card
                termdef = (1 - termdef)  # toggle termdef

            elif go == 'b':
                idx -= 1
                termdef = 0  # reset card back to show term

            elif go == 't':  # change default to definition first or term first
                td_default = (1 - td_default)  # toggle default
                termdef = td_default  # set current card to new default
            
            elif go == '':
                idx += 1
                termdef = td_default  # reset card back to show term

            go = ''

        exit_program()
    
    else:
        print("File Not Found, Exiting.")
        exit_program()

def create_mode(filename): # create and save new flashcards to a file (can't edit existing files)

    if(find_json(filename)):
        print("File already exists, please use edit mode to modify existing files.")
        exit_program()

    data = {}

    go = "y"

    while(go != 'q'):
        
        term = input("Enter the new term: ")

        if term == 'q':
            clear_screen()
            save_and_exit(filename, data)

        definition = input("Enter the new definition: ")

        if definition == 'q':
            save_and_exit(filename, data)

        data[term] = definition

        go = input("Continue (enter), or quit (q).")
    
    save_and_exit(filename, data)
        

def edit_mode(filename): # edit existing flashcards in a file

    #set = FlashcardSet()
    data = read_json(filename)
    if(data != None):
        # successfull file reading
        go = ""
        idx = 0
        clear_screen()

        keys = list(data.keys())
        values = list(data.values())

        while go != 'q':  # program should continue

            clear_screen()

            if(idx > len(keys) - 1):  # loop back to start
                idx = 0
            

            print("Term: ", keys[idx], '\n')
            print("Definition: ", data[keys[idx]], '\n')

            go = input("next (enter), edit card (e), delete card (d), back (b), quit (q): ")
            
            if go == 'b':
                idx -= 1

            if go == 'd':
                confirm = input("Are you sure you want to delete this card? (y/n): ")
                if confirm == 'y':
                    del data[keys[idx]]
                    keys = list(data.keys())  # update keys list
                    if(idx > len(keys) - 1):
                        idx = 0  # loop back to start if we deleted the last card
                    else: idx += 1
                save_json(filename, data)  # save after deletion
                
            if go == 'e':
                pass # edit card function to be implemented
            if go == "":
                idx += 1
                
    else:
        print("File Not Found, Exiting.")
        save_and_exit(filename, data)  # redundant but safe


def edit_card(data, key): # edit a specific card in the dictionary
    pass

def main():

    try:

        if(len(sys.argv) < 2):  # no arguments
            print("Unexpected Arguments. usage: fcm <mode> <filename>")
            print("For more information, use: fcm help")
            exit()

        if(sys.argv[1] == 'help'): # we have at least one argument
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
                    edit_mode(filename)

                case "q":
                    exit_program()

                case _:
                    print("Invalid Mode Selected, Entering Practice Mode.")

    except TypeError:
        print("Error, Invalid Arguments. Exiting.")
    # at this point we have either exited because of error or continued with a mode flag selected

main()
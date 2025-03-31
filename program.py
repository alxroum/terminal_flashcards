import display_card as dc
import sys
import json
import os

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

    #set = FlashcardSet()
    data = read_json(filename)
    if(data != None):
        # successfull file reading
        go = ""
        idx = 0
        clear_screen()

        keys = list(data.keys())
        termdef = 0  # 0 for term, 1 for definition

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

            print(dc.display_card(line, 26, 2, 2))

            go = input("next (enter), flip (f), back (b), quit (q): ")

            if go == 'q':
                clear_screen()
                exit_program()
            
            elif go == 'f':  # flip term and loop again, without going to the next card
                if termdef == 1: termdef = 0;
                else: termdef = 1

            elif go == 'b':
                idx -= 1
                termdef = 0  # reset card back to show term
            
            elif go == '':
                idx += 1
                termdef = 0  # reset card back to show term

            go = ''

        exit_program()
    
    else:
        print("File Not Found, Exiting.")
        exit_program()

def create_mode(filename):

    data = read_json(filename)
    if(data != None):
        go = "y"

        while(go != ''):
            
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

def edit_mode(filename):

    #set = FlashcardSet()
    data = read_json(filename)
    if(data != None):
        # successfull file reading
        go = ""
        idx = 0
        clear_screen()

        keys = list(data.keys())
        values = list(data.values())
        termdef = 0  # 0 for term, 1 for definition

        while go == "":  # program should continue

            #clear_screen()

            if(idx > len(keys) - 1):  # loop back to start
                idx = 0
            if(idx < 0):
                idx = len(keys) - 1  # loop to end

            line = ''

            if termdef == 0:
                line = keys[idx]
            else:
                line = data[keys[idx]]

            print(dc.display_card(line, 26, 2, 2))

            go = input("next (enter), flip (f), back (b), quit (q), edit (e), delete (d): ")

            if go == 'e':
                if termdef == 0:  # editing term
                    new_term = input("You are changing the card's term. What would you like to change it to?\n")

                    if new_term != '':
                        keys[idx] = new_term
                        # create new dict from stored lists
                        data = dict(zip(keys, values))
                        save_json(filename, data)
                        data = read_json(filename)
                else:  # editing definition
                    new_def = input("You are changing the card's definition. What would you like to change it to?\n")

                    if new_def != '':
                        data[keys[idx]] = new_def
                        save_json(filename, data)
                        data = read_json(filename)
                

            if go == 'd':
                pass

            if go == 'q':
                clear_screen()
                save_and_exit(filename, data)
            
            elif go == 'f':  # flip term and loop again, without going to the next card
                if termdef == 1: termdef = 0;
                else: termdef = 1

            elif go == 'b':
                idx -= 1
                termdef = 0  # reset card back to show term
            
            elif go == '':
                idx += 1
                termdef = 0  # reset card back to show term

            go = ''

        save_and_exit(filename, data)
    
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
                    edit_mode(filename)

                case "q":
                    exit_program()

                case _:
                    print("Invalid Mode Selected, Entering Practice Mode.")

        else:
            print("Unexpected Arguments. usage: fcm <mode> <filename>")
            exit()
    except TypeError:
        print("Error, Invalid Arguments. Exiting.")
    # at this point we have either exited because of error or continued with a mode flag selected

main()
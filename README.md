# <b>Terminal Flashcards (TFC)</b>

<img src="graphics/icon.png" alt="terminal flashcards logo" width="500" title="terminal flashcards logo"> 

<br>

## <b>About TFC</b>
This project was created to simplify the process of studying flashcards. Typically you have to make accounts, go to websites, deal with ads, etc. Now, you can create and study custom flashcard sets right in your terminal!

All flashcard sets are stored in .json files. A save file will be created if you create it with tfc, or you can import your own. See [save file formatting](#file_formatting) for details.
<br>

## <b>Getting Started</b>

The simplest way to get started is to download the tfc excecutable.

### <b>Download the Exe</b>

or, clone the project.

### <b>Clone Project</b>
```sh
git clone https://github.com/alxroum/terminal_flashcards.git
```
<br>

### <b>Usage</b>
```
Modes: practice (pr), create (cr), edit (em)
Filename: exclude file extension (file should be a json file)
```
### <b>Modes</b>

There are 3 modes available to use:
- Practice Mode
    - Practice mode allows you to view flashcards' terms and definitions.
- Create Mode
    - Create mode allows you to add new cards to the set.
- Edit Mode
    - Edit mode allows you to change a term, definition, or both as well as delete cards from the set.

<br>

### <b>Run With Python</b>
```sh
py program.py <mode> <filename>
``` 
<br>

### <b>Run With Executable</b>
```
tfc.exe <mode> <filename>
```
### <b>Run the manager with my_file in practice mode:</b>
```sh
tfc pr my_file
```

<br>

<a name="file_formatting"></a>
### <b>Save File Formatting</b>

All flashcard sets are saved in ```.json``` files. All files have terms and definitions stored as shown below:
```my_flashcard_set.json```
``` json
{
    "Term1": "Definition1",
    "Term2": "Definition2",
    "Term3": "Definition3",
    "Term4": "Definition4",
    "Term5": "Definition5",
    "Term6": "Definition6"
}
```
<br>

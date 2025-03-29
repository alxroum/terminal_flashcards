# <b>Terminal Flashcards</b>

<img src="graphics/icon.png" alt="terminal flashcards logo" width="500" title="terminal flashcards logo"> 

<br>

## <b>About</b>
This project was created to simplify the process of studying flashcards. Having to make accounts, go to websites, ads, etc. Now, you can create and study custom flashcard sets right in your terminal!

All flashcard sets are stored in .json files. The program will save one for you if you create it with this program, or you can import your own. See [save file formatting](#file_formatting) for details.
<br>

## <b>Getting Started</b>
<br>

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
<br>

### <b>Run With Python</b>
```sh
py program.py <mode> <filename>
``` 
<br>

### <b>Run With Executable</b>
```
fcm.exe <mode> <filename>
```
### <b>Run the manager with my_file in practice mode:</b>
```sh
fcm pr my_file
```

<br>

<a name="file_formatting"></a>
### <b>Save File Formatting</b>

All flashcard sets are saved in ```.json``` files. All files have terms and definitions as shown below:

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
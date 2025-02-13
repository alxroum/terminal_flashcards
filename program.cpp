#include <bits/stdc++.h>
using namespace std;


class Flashcard {

    private:
        string term; // flashcard front side or term
        string def; // flashcard back side or definition

    public:
        Flashcard(string term, string def) {
            this->term = term;
            this->def = def;
        }

        string getTerm() {
            return this->term;
        }

        string getDef() {
            return this->term;
        }

        void setTerm(string term) {
            this->term = term;
        }

        void setDef(string def) {
            this->def = def;
        }

        void printTerm() {
            cout << this->term << endl;
        }

        void printDef() {
            cout << this->def << endl;
        }

        void printBoth() {
            cout << endl;
            cout << this->term << " --> " << this->def << endl;
            cout << endl;
        }
};

class FlashcardSet {

    private:
        string *cards;

    public:
};

void createFlashcards() {

}

void practiceSet() {

    string go = "\n";
    int idx = 0;

    while(go == "\n") {
        // do something
        cout << "Next Card" << endl;

        go = std::cin.get();
        idx++;
    }
    cout << "Exiting." << endl;
    return;
}

void viewSet() {

}

void createCards() {

}

void drawCard() {
    cout << ".-------------------------." << endl;
    cout << "|                         |" << endl;
    cout << "|                         |" << endl;
    cout << "|        test text        |" << endl;
    cout << "|                         |" << endl;
    cout << "|                         |" << endl;
    cout << "'-------------------------'" << endl;
    return;
}

string splitLines(string s, int maxLineLength) { // takes a string of text and splits it into equal lines based on a max line length
    // add "\n" to string in places where line breaks should occur
    // split string into words
    // create single string again from strings, but put line breaks to make lines
    
}

int main(int argc, const char* argv[]) {

    int _prMode = 0; // practice mode flag
    int _crMode = 0; // create mode flag
    int _vwMode = 0; // view mode flag

    if(argc > 1) { // set flags

        if(strcmp(argv[1], "pr") == 0) {
            // practice set mode;
            cout << "Practice Mode:" << endl;
            _prMode = 1;
        } 
        if(strcmp(argv[1], "cr") == 0) {
            // practice set mode;
            cout << "Create Mode:" << endl;
            _crMode = 1;
        } 
        if(strcmp(argv[1], "vw") == 0) {
            // practice set mode;
            cout << "View Mode:" << endl;
            _vwMode = 1;
            drawCard();
            cout << splitLines("This is a test card in which I will test the splitlines function", 15) << endl;
        } 
    } else {
        cout << "View Mode:" << endl;
        _vwMode = 1;
    }
}

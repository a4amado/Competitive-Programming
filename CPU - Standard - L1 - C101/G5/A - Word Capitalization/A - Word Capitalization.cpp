#include <iostream>
#include <string>

using namespace std;

int main() {



    string word = "";
    getline(cin, word);

    if ((int)word.at(0)> 90) {
        word[0] =  (char) (word.at(0) - 32);
    }


    cout << word << endl;

    return 0;
}
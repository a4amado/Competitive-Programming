
#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {

    int n;
    cin >> n;
    cin.ignore();
    set<char> s;
    
    for (int i = 0; i < n; i++) {
        int char_that_should_be_x = (n - i) - 1;
        int other_char_that_should_be_x = i;

        string l;

        getline(cin, l);

        for (int j = 0; j < l.size(); j++) {
            s.insert(l.at(j));

            if (j == char_that_should_be_x || j == other_char_that_should_be_x) {
                continue;
            }

            if (l.at(j) == l.at(char_that_should_be_x)) {
                cout << "NO" << endl;
                return 0;
            }
        }


        if (l.at(char_that_should_be_x) != l.at(other_char_that_should_be_x)) {
            cout << "NO" << endl;
            return 0;
        }
    }
 

    if (s.size() != 2) {
        cout << "NO" << endl;
        return 0;
    }
    cout << "YES" << "\n";
 
    return 0;
}

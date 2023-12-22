#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;

    cin.ignore();
    string s = "";
    getline(cin, s);


    int o = 0;
    for (int i = 0; i < s.length() - 1; i++) {
        if (s[i] == s[i + 1] ) {
            s[i] = s[i + 1];
            o++;
        }
    }


    cout << o << endl;


    return 0;
}
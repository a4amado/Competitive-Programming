#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
   
    string s = "";
    getline(cin, s);
    map<char, int> f;

    int y = 0;
    for (int i = 0; i < s.length() - 1; i++) {
        if (s.at(i) == '}' || s.at(i) == '{' || s.at(i) == ' ' || s.at(i) == ',' ) {
            continue;
        }else  if (f[s.at(i)] !=1 ) {
            y++;
            f[s.at(i)] = 1;
        }
    }

     cout << f.size() << endl;


    return 0;
}
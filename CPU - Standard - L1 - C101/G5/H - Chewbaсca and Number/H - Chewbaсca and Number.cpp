#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main()
{

    string s;
    cin >> s;

    for (int i = 0; i < s.size(); i++)
    {

        if ((s[i] - '0') > 4)
        {
            s[i] = char(9 - (s[i] - '0'));
        }
    }

    if (s.front() == '0')
    {
        s.front() = '9';
    }

    cout << s << endl;
    return 0;
}

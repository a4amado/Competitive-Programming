/**
 * name: Police Recruits
 * link: https://codeforces.com/contest/427/problem/A
 */

#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore();

    string line;
    getline(cin, line);

    char delimiter[] = " ";
    char *token;

    char *cstr = new char[line.length() + 1];
    strcpy(cstr, line.c_str());

    line.clear();

    int un_treated_crimes = 0;
    int officers_available = 0;

    token = strtok(cstr, delimiter);

    while (token != NULL)
    {
        if (atoi(token) == -1)
        {
            if (officers_available > 0)
            {
                officers_available--;
            }
            else
            {
                un_treated_crimes++;
            }
        }
        else
        {
            officers_available = officers_available + atoi(token);
        }

        token = strtok(NULL, delimiter);
    }

    cout << un_treated_crimes << endl;
    delete[] token;

    return 0;
}

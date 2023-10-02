/**
 * Name: Night at the Museum
 * link: https://codeforces.com/contest/731/problem/A
 */

#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;
int main()
{

    string name;
    getline(cin, name);

    int steps = 0;

    int position = 97;
    for (int i = 0; i < name.length(); i++)
    {

        int int_of_char = (int)name[i];

        int diff = abs(int_of_char - position);

        if (diff < 13)
        {
            steps += diff;
        }
        else
        {
            int forced_small_diff = abs(26 - diff);
            steps += forced_small_diff;
        };
        position = int_of_char;

    }

    cout << steps << endl;

    return 0;
}

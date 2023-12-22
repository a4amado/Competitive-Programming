#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{

    map<char, int> mm;

    mm.insert(make_pair('A', 0));
    mm.insert(make_pair('B', 0));
    mm.insert(make_pair('C', 0));

    char bigger_than = '>';
    char less_than = '<';

    for (int i = 0; i < 3; i++)
    {
        string s;
        getline(cin, s);

        char first = s.at(0);
        char sign = s.at(1);
        char last = s.at(2);

        if (sign == bigger_than)
        {
            mm[first] = mm[first] + 1;
        }
        else
        {
            mm[last] = mm[last] + 1;
        }
    }

    char d[3];


    for (int i = 0; i < 3; i++)
    {
        if (mm['A'] == 0)
        {
            d[0] = 'A';
        }
        else if (mm['A'] == 1)
        {
            d[1] = 'A';
        }
        else if (mm['A'] == 2)
        {
            d[2] = 'A';
        }
        if (mm['B'] == 0)
        {
            d[0] = 'B';
        }
        else if (mm['B'] == 1)
        {
            d[1] = 'B';
        }
        else if (mm['B'] == 2)
        {
            d[2] = 'B';
        }


        if (mm['C'] == 0)
        {
            d[0] = 'C';
        }
        else if (mm['C'] == 1)
        {
            d[1] = 'C';
        }
        else if (mm['C'] == 2)
        {
            d[2] = 'C';
        }
    }


    if (mm['A'] == 1 && mm['B'] == 1 && mm['C'] == 1) {
        cout << "Impossible" << endl;
        return 0;
    }
    for (auto ss : d)
    {
        cout << ss ;
    }
    return 0;
}

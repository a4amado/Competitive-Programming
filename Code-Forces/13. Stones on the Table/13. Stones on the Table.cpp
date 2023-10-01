#include <iostream>
#include <string>
using namespace std;

int main()
{

    int size;
    cin >> size;

    string c;
    cin >> c;

    int d = 0;
    for (int i = 0; i < c.length() - 1; i++)
    {
        char c_item = c.at(i);
        char n_item = c.at(i + 1);
        if (c_item == n_item)
        {
            d++;
        }
    }

    cout << d << endl;
    return 0;
}
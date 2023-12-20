#include <iostream>
#include <string>

using namespace std;

int main()
{

    string n;
    getline(cin, n);

    if (n.length() < 2)
    {
        cout << 0 << endl;
        return 0;
    }

    int counter = 0;

    while (n.length() > 1)
    {
        int sum = 0;
        for (int i = 0; i < n.length(); i++)
        {
            sum += n.at(i) - '0';
        }
        n = to_string(sum);

        if (n.length() >= 1) {
                        counter++;

        }

        
    }


    cout << counter << endl;
    return 0;
}
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore();

    vector<string> l;

    for (int i = 0; i < n; i++)
    {

        string r;
        getline(cin, r);
        l.push_back(r);
    }

    for (int i = 0; i < l.size(); i++)
    {
        string t;
        t.push_back(l.at(i).at(0));

        for (int j = 1; j < l.at(i).size() - 1; j++)
        {
            if (j % 2 == 0) {
                t.push_back(l.at(i).at(j));
            }
        }
        
        t.push_back(l.at(i)[l.at(i).length() -1 ]);
        l[i] = t;
    }

    for (auto i: l) {
        cout << i << endl;
    }
    return 0;
}
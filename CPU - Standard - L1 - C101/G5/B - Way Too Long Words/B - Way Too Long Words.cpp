#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{

    int num = 0;
    cin >> num;
    vector<string> nn;
    cin.ignore();
    
    for (int i = 0; i < num; i++)
    {
        string f = "";
        getline(cin, f);
        nn.push_back(f);
    }

    for (int i = 0; i < nn.size(); i++)
    {

        if (nn[i].length() <= 10)
        {
            cout << nn[i] << endl;
            continue;
        }

        char f_char = nn[i][0];
        char l_char = nn[i][nn[i].length() - 1];
        int len = nn[i].length() - 2;

        nn[i].clear();

        nn[i].push_back(f_char);
        nn[i] = nn[i] + to_string(len);
        nn[i].push_back(l_char);

        cout << nn[i] << endl;
    }

    return 0;
}

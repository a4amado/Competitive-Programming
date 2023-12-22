#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{

    int n, max;
    cin >> n >> max;
    cin.ignore();

    int r = n;
    for (int i = 0; i < n; i++)
    {
        string s;
        getline(cin, s);

        if (s.size() < max)
        {
            r--;
            continue;
        }
        else
        {

            for (int j = 0; j < s.size(); j++)
            {
                if (s.find(to_string(j)) != string::npos)
                {
                    r--;
                    continue;
                }
            }
        }
    }

    cout << r << endl;
  return 0;
}

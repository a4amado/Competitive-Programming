#include <iostream>

using namespace std;

int main()
{

    int n;
    cin >> n;
    int l_1[n];

    for (int i = 0; i < n; i++)
    {
        cin >> l_1[i];
    }

    int m;
    cin >> m;
    int l_2[m];
    for (int i = 0; i < m; i++)
    {
        cin >> l_2[i];
    }

    int g = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; i++)
        {
            g++;
            if (l_2[i] == l_1[j]) {
                break;
            }
        }
    }

    int b = 0;
    for (int i = 0; i < m; i++)
    {
        for (int j = n - 1; j >= 0; j--)
        {
            b++;
            if (l_1[j] ==l_2[i]) {
                break;
            }
        }
    }

    cout << g << " " << b << endl;
    return 0;
}
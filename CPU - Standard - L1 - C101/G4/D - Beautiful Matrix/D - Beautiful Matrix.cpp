#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int n = 5;

    int x, y;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int g = 0;

            cin >> g;

            if (g == 1)
            {
                x = i;
                y = j;
            }
        }
       
    }

    int e = abs(x - 2) + abs(y - 2);

    cout << e << endl;

    return 0;
}

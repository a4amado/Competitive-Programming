#include <iostream>

using namespace std;

int main()
{

    int n;
    cin >> n;

    int *list = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> list[i];
    }

    int start, end;

    cin >> start >> end;

    for (int i = start  -1 ; i < end; i++)
    {
        cout << list[i] << " ";
    }

    return 0;
}

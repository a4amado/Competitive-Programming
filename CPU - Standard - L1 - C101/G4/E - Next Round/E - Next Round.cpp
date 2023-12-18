#include <iostream>

using namespace std;

int main()
{
    int n, k;

    cin >> n >> k;
    k--;
    int num_of_qualifiers = 0;

    int *arr = new int[n];
 
    for (int i = 0; i < n; i++)
    {
      cin >> arr[i];
    }

 
    for (int i = 0; i < n; i++)
    {
        if (arr[i] >= arr[k] && arr[i] > 0)
        {
            num_of_qualifiers++;
        }
    }

    cout << num_of_qualifiers << endl;
    return 0;
}

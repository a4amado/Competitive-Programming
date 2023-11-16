#include <iostream>

using namespace std;

int check(int *list, int n, int length);
int main()
{

    int n;
    cin >> n;

    int *heights = new int[n];
    int *a = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> heights[i];
    }

    for (int i = 0; i < n; i++)
    {
        a[i] = check(heights, i, n);
    }

    // TODO: write a function that get the highst last digit in the array, add 1 and print.

    return 0;
}

int check(int *list, int n, int length)
{
    int current = 0;

    // Check elements from index n to 1
    for (int i = n; i > 0; i--)
    {
        int current_num = list[i];
        int compared_item = list[i - 1];
        if (current_num >= compared_item)
        {
            current++;
        }
        else
        {
            break;
        }
    }

    for (int i = n; i < length - 1; i++)
    {
        int current_num = list[i];
        int compared_item = list[i + 1];
        if (current_num >= compared_item)
        {
            current++;
        }
        else
        {
            break;
        }
    }

    return current;
}

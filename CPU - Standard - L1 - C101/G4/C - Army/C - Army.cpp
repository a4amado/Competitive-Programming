#include <iostream>

using namespace std;

int main()
{

    int n;
    cin >> n;

    int *years_to_promotion_per_rank = new int[n];

    for (int i = 0; i < n - 1; i++)
    {
        cin >> years_to_promotion_per_rank[i];
    }

    int starting_rank, end_rank;

    cin >> starting_rank >> end_rank;

    end_rank = end_rank - 2;
    starting_rank = starting_rank - 1;

    int final = 0;
    for (int i = starting_rank; i <= end_rank; i++)
    {
        final += years_to_promotion_per_rank[i];
    }

    cout << final << endl;
    return 0;
}
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{

    long long dollars = 0;
    
    long long dollars_SPENT = 0;
    long long n = 0;
    cin >> n;

    long long *plyons = new long long[n];
 
    for (long long i = 0; i < n; i++)
    {
        cin >> plyons[i];
    };

     
    dollars_SPENT = plyons[0];

    
    for (long long i = 0; i < n - 1; i++)
    {
        long long diff_with_next_plyon = plyons[i + 1] - plyons[i];
        long long dollars_i_need_to_spend_this_time = abs(dollars - abs(diff_with_next_plyon));

        // if jumping up
        if (diff_with_next_plyon > 0)
        {
            // if dont't have enough dollars
            if ((abs(diff_with_next_plyon)) > dollars)
            {
                dollars_SPENT = dollars_SPENT + abs(dollars_i_need_to_spend_this_time);
                dollars = 0;
            }
            else
            {
                dollars = dollars - abs(diff_with_next_plyon);
            }
        }
        else
        {
            dollars = dollars + abs(diff_with_next_plyon);
        }
    }

    cout << dollars_SPENT << endl;

    return 0;
}
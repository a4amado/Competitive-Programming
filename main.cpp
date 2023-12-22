#include <iostream>
#include <math.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <numbers>
#include <map>

using namespace std;
int climbStairs(int n)
    {
        map<char, int> memo;
        memo['l'] = 0;
        memo['b'] = 0;

        int ref = n;
        while (n >= 0)
        {
            if (ref == n) {
                memo['l'] = 1;
            } else  if (n == ref - 1) {
                memo['b'] = 1;
            } else {
                int new_h = memo['b'] + memo['l'];
                memo['b']  = memo['l'];
                memo['l'] = new_h;

            }

            n--;
        }

        return memo['l'];
    }
int main()
{

    cout << climbStairs(2) << endl;

    return 0;
}
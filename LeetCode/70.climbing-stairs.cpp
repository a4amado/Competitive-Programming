/*
 * @lc app=leetcode id=70 lang=cpp
 *
 * [70] Climbing Stairs
 */
#include <iostream>
#include <map>

using namespace std;

// @lc code=start
class Solution
{

public:
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
};
// @lc code=end

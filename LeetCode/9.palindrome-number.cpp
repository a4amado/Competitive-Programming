/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

// @lc code=start
class Solution {
public:
    
    bool isPalindrome(int x) {
        string num = to_string(x);
        int i, j;
        j = num.length() - 1;
        i = 0;

        
        for (;;) {
            if (num[j] != num[i]) {
                return false;
            };

            if (i == ceil(num.length() / 2)) {
                break;
            }

            i++;
            j--;

        }

        


        return true;
    }
};
// @lc code=end


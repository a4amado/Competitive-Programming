/*
 * @lc app=leetcode id=66 lang=cpp
 *
 * [66] Plus One
 */
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// @lc code=start
class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        int last_digit = digits.back();

        if (last_digit == 9)
        {

            for (int i = digits.size() - 1; i >= 0; i--)
            {
                if (digits[i] == 9)
                {
                    digits[i] = 0;
                    if (i == 0)
                    {
                        digits[i] = 1;
                        digits.push_back(0);
                        break;
                    }
                } else {
                    digits[i]++;
                    break;
                }
            }
            return digits;
        }
        digits[digits.size() - 1]++;

        return digits;
    }
};
// @lc code=end

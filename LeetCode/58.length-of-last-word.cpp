/*
 * @lc app=leetcode id=58 lang=cpp
 *
 * [58] Length of Last Word
 */
#include <iostream>
#include <string>

using namespace std;

// @lc code=start
class Solution
{
public:
    int lengthOfLastWord(string s)
    {

        if (s.length() == 1)
        {
            return 1;
        }
        int high = s.length() - 1;
        int low = high;

        while (true)
        {

            if (s[high] == ' ')
            {
                high--;
                low--;
            }  else if 
        }
    }
};
// @lc code=end

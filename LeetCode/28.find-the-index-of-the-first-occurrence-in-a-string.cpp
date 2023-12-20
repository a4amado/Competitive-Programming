/*
 * @lc app=leetcode id=28 lang=cpp
 *
 * [28] Find the Index of the First Occurrence in a String
 */
#include <iostream>

#include <string>

using namespace std;

// @lc code=start
class Solution {
public:

int strStr(string haystack, string needle)
{
    if (needle.size() > haystack.size())
    {
        return -1;
    }
    int i = 0;
    while (i < haystack.size() &&(haystack.size() -  (i > needle.size())))
    {
        if ((haystack.size() - i) < needle.size())
        {
            return -1;
        }
        string f = haystack.substr(i,  needle.size());
        if (f == needle)
        {
            return i;
        }
        i++;
    }

    return -1;
}
};
// @lc code=end


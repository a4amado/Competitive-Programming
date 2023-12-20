/*
 * @lc app=leetcode id=14 lang=cpp
 *
 * [14] Longest Common Prefix
 */
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
// @lc code=start
class Solution
{
public:
    
string longestCommonPrefix(vector<string> &strs) {
    if (strs.empty()) {
        return "";
    }

    string prefix = strs[0];

    for (int i = 1; i < strs.size(); i++) {
        int j = 0;
        while (j < prefix.length() && j < strs[i].length() && prefix[j] == strs[i][j]) {
            j++;
        }

        prefix = prefix.substr(0, j);

        if (prefix.empty()) {
            break;  // No common prefix found
        }
    }

    return prefix;
}

    
};
// @lc code=end

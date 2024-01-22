/*
 * @lc app=leetcode id=859 lang=cpp
 *
 * [859] Buddy Strings
 */
#include <iostream>
#include <string>

using namespace std;

// @lc code=start
class Solution {
public:
    bool buddyStrings(string s, string goal) {
        int diff = 0;
        if (s.length() != goal.length()) {
            return false;
        }
        


        
        for (int i = 0; i < s.length(); i++) {
            if (s.at(i) != goal.at(i)) {
                diff++;
            }
        }
       
        if (diff != 2) {
            return false;
        }

        return true;
    }
};
// @lc code=end


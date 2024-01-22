/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 */
#include <iostream>
#include <string>
#include <map>
using namespace std;

// @lc code=start
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        map<int, int> l;
        for (char c: t) {
            if (!l[(int) c]) {
                l[(int) c] = 1;
            } else {
                l[(int) c] += 1;
            }
        }
        bool tt;
        for (char c: s) {
            if (!l[(int) c]) {
                return false;
            } else {
                l[(int) c] -= 1;
            }
        }

        return true;
    }
};
// @lc code=end


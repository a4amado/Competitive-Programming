/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        String longest = "";
        for (int i = 0; i < s.length(); i++) {
            String curr = this.longestPalindormeWhereXisItsCenter(s, i);
            if (curr.length() > longest.length()) {
                longest = curr;
            }
        }
        return longest;
    }

    static String longestPalindormeWhereXisItsCenter(String s, Integer idx) {
        Integer r = idx;
        Integer l = idx;

        if (s.length() % 2 == 0) {
            r = (s.length() / 2) - 1;
            l = (s.length() / 2);
        }

        Integer c_l = l;
        Integer c_r = r;

        if (s.length() % 2 == 0) {
            while (l > -1 || r < s.length()) {
                if (s.charAt(l) == s.charAt(r)) {
                    c_l = l;
                    c_r = r;
                    l--;
                    r++;
                } else {
                    
                }
            }
        }
        if (s.length() % 2 != 0) {
            while (l > -1 && r < s.length()) {

            }
        }

        return s.substring(c_l, c_r + 1);
    }
}
// @lc code=end

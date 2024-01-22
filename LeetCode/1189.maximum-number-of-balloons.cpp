/*
 * @lc app=leetcode id=1189 lang=cpp
 *
 * [1189] Maximum Number of Balloons
 */
#include <iostream>
#include <map>
#include <string>


using namespace std;

// 97 to 122,

// @lc code=start
class Solution
{
public:
    int maxNumberOfBalloons(string text)
    {
        int freq_arr[26] = {0};

        for (char i : text)
        {
            int idx = (int)tolower(i) % 97;
            freq_arr[idx]++;
        }

        map<char, int> zip = {{'b', 1},
                               {'a', 1},
                               {'l', 2},
                               {'o', 2},
                               {'n', 1}};

        int min_n = 0;

        for (auto b : zip)
        {
            int idx = (int)tolower(b.first) % 97;
            int number_chars_we_have = freq_arr[idx];
            int number_of_char_we_need_for_1 = b.second;
            if (number_chars_we_have < number_of_char_we_need_for_1) return 0;

            if (min_n == 0) {
                min_n = number_chars_we_have / number_of_char_we_need_for_1;
                continue;
            }
            min_n = min(min_n, number_chars_we_have / number_of_char_we_need_for_1);
        }
        return min_n;
    }
};

// @lc code=end

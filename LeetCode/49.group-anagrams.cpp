/*
 * @lc app=leetcode id=49 lang=cpp
 *
 * [49] Group Anagrams
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
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        map<string, vector<int>> mm;
        int i = 0;
        for (auto &item : strs)
        {
            string key = item;
            sort(key.begin(), key.end());

            if (mm.find(key) == mm.end())
            {
                mm.emplace(key, std::vector<int>{i});
            }
            else
            {
                mm[key].push_back(i);
            }

            i++;
        }
        // construct a new array
        vector<vector<string>> ll;
        for (const auto &pair : mm)
        {
          vector<string> item;
          for (const auto& l_item: pair.second) {
            item.push_back(strs[l_item]);
          }
          ll.push_back(item);
        }
        return ll;
    }
};


// @lc code=end

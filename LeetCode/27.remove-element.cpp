/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        sort(nums.begin(), nums.end());

        int j = 0;
        
        // get the first item where the deletion wil start
        while (j < nums.size() && nums[j] != val) {
            j++;
        };


        int i = j;
        // get the second item where the deletion wil ends
        while (i < nums.size() && nums[i] == val) {
            i++;
        };


        while (i < nums.size()) {
            nums[j++] = nums[i++];
        }


        nums.resize(j);

        return j;
    }
};
// @lc code=end

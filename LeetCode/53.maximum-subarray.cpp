/*
 * @lc app=leetcode id=53 lang=cpp
 *
 * [53] Maximum Subarray
 */

// @lc code=start

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
         int max_sub = nums[0];
    int currunt_max = 0;


    for (int i = 0; i < nums.size(); i++) { 
        // if curr < 0 return to z;
        currunt_max = max(currunt_max, 0);

        currunt_max = currunt_max + nums[i];

        max_sub = max(max_sub, currunt_max);
    }
    return max_sub;
    }
};
// @lc code=end


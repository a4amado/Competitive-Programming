/*
 * @lc app=leetcode id=35 lang=cpp
 *
 * [35] Search Insert Position
 */
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution
{
public:
int searchInsert(vector<int> &nums, int target)
{
    int i = 0;
    int j = nums.size() - 1;
    int pos = -1;
    int middle = (j + i) / 2;

    if (target > nums[nums.size()])
    {
    }
    while (i <= j)
    {

        if ( target == nums[middle]) {
            return middle;
        }


        if (target < nums[middle])
        {
            j = middle - 1;
            middle = (j + i) / 2;
        }
        else if (target > nums[middle])
        {
            i = middle + 1;
            middle = (j + i) / 2;
        }
    }
    return i;
}

};
// @lc code=end

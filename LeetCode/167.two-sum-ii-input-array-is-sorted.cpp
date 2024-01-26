/*
 * @lc app=leetcode id=167 lang=cpp
 *
 * [167] Two Sum II - Input Array Is Sorted
 */
#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int left = 0;
        int right = numbers.size() - 1;
        vector<int> d;
        while (left <= right)
        {
            if (numbers.at(left) + numbers.at(right) == target)
            {

                d.push_back(left + 1);
                d.push_back(right + 1);
                break;
            }
            else if (numbers.at(left) + numbers.at(right) > target)
            {
                right--;
            }
            else
            {
                left++;
            }
        }

        return d;
    }
};
// @lc code=end

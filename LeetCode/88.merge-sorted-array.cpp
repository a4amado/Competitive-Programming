/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// @lc code=start

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int delete_items_1 = 0;
        int shoud_be_deleted = nums1.size() - m;
        for (int i = nums1.size() - 1; i >= 0; i--)
        {
            if (delete_items_1 >= shoud_be_deleted)
            {
                break;
            }
            if (nums1[i] == 0)
            {
                nums1.erase(nums1.begin() + i);
                delete_items_1++;
            }
            else
            {
                break;
            }
        }

        delete_items_1 = 0;
        shoud_be_deleted = nums2.size() - n;
        for (int i = nums2.size() - 1; i >= 0; i--)
        {
            if (delete_items_1 >= shoud_be_deleted)
            {
                break;
            }
            if (nums2[i] == 0)
            {
                nums2.erase(nums2.begin() + i);
            }
            else
            {
                break;
            }
        }

        vector<int> e;

        while (!nums1.empty() && !nums2.empty())
        {

            if (nums1.front() < nums2.front())
            {
                e.push_back(nums1.front());
                nums1.erase(nums1.begin());
            }
            else if (nums1.front() > nums2.front())
            {
                e.push_back(nums2.front());
                nums2.erase(nums2.begin());
            }
            else if (nums1.front() == nums2.front())
            {
                e.push_back(nums1.front());
                e.push_back(nums2.front());
                nums1.erase(nums1.begin());
                nums2.erase(nums2.begin());
            }
        }

        while (nums1.size() > 0)
        {
            e.push_back(nums1.front());
            nums1.erase(nums1.begin());
        }
        while (nums2.size() > 0)
        {
            e.push_back(nums2.front());
            nums2.erase(nums2.begin());
        }

        sort(e.begin(), e.end());
        nums1 = e;
    };
};

// @lc code=end

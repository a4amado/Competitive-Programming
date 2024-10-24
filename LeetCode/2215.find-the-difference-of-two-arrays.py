#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        l_1 = []
        for i in nums1:
            if i not in nums2: l_1.append(i)
        l_2 = []
        for i in nums2:
            if i not in nums1: l_2.append(i)
        return [l_1, l_2]

# @lc code=end


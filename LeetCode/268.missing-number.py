# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNumber = 0
        m = {}

        for num in nums:
            maxNumber = max(maxNumber, num)
            m[num] = True

        for i in range(len(nums) + 1):
            if i not in m:
                return i
        return 1
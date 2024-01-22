#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        tips = 0
        # find tips of the mounten
        for i in range(len(arr)):
            if i == 0:
                curr = arr[i]
                after = arr[i + 1]
                if curr >= after:
                    return False
            elif i == len(arr) - 1:
                curr = arr[i]
                before = arr[i - 1]
                if before <= curr:
                    if tips > 0:
                        return False
            else:
                before = arr[i - 1]
                curr = arr[i]
                after = arr[i + 1]
                if (curr > after and curr > before) or (curr < after and curr < before) or (curr == before) or curr == after:
                    tips += 1
        if tips == 0:
            return False
        if tips > 1:
            return False
        return True


# s = Solution()
# print(s.validMountainArray([0,1,2,3,4,5,6,7,8,9]
# ))

# @lc code=end

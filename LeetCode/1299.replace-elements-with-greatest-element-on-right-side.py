#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

from typing import *
# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        carry = -1
        for idx in range(len(arr) -1, -1, -1):
            temp = arr[idx]
            arr[idx] = carry
            carry = max(carry, temp)

        return arr
# @lc code=end

arr = [17,18,5,4,6,1]

sol = Solution()

print(sol.replaceElements(arr))

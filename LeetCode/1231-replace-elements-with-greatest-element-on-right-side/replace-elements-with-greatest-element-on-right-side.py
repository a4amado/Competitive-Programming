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
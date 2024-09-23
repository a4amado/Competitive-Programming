#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

from typing import List


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        carry = 1
        idx = len(digits) - 1
        while carry == 1:
            if digits[idx] == 9:
                while idx >= 0 and digits[idx] == 9 and carry == 1:
                    digits[idx] = 0
                    idx -= 1
                    carry = 1
                
                    
            else:
                digits[idx] += 1 
                idx -= 1
                carry = 0
            
            if idx < 0 and carry == 1:
                digits.insert(0, 1)
                carry = 0
                idx -= 1
        return digits
            
# @lc code=end

s = Solution()
print(s.plusOne([9,9]))
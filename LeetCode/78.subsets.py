#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def b(start: int, currunt: List[int]):
            res.append(currunt.copy())

            for end in range(start, len(nums)):
                currunt.append(nums[end])
                b(end + 1, currunt)
                currunt.pop()

                
                    
            
        b(0, [])

        return res
# @lc code=end

s = Solution()
s.subsets([1,2,3])
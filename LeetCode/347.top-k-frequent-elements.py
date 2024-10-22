#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from collections import Counter
from typing import *

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArra = Counter(nums)
        l = [
            [freq, n] for n, freq in freqArra.items()
        ]
        l.sort(reverse=True)
        
        
        return[
            item for _, item in l[:k]
        ]
        
# @lc code=end

nums = [1,1,1,2,2,3]
k = 2

sol = Solution()

print(
    sol.topKFrequent(nums, k)
)
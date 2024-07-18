#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from collections import Counter
from heapq import heappush, heappop, _heapify_max

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArra = Counter(nums)
        min_heap = []
        
        for num, freq in freqArra.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)
        
        top_k_frequent =  [pair[1] for pair in min_heap]
        return top_k_frequent
        
# @lc code=end


#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

from typing import List
import heapq 


# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxHeap= []
        for i in stones:
            heapq.heappush(maxHeap, -i)
        while len(maxHeap) >= 2:
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            if y == x:
                continue
            else:
                heapq.heappush(maxHeap, -abs(y - x))
        return -maxHeap[0] if  stones else 0
        
# @lc code=end

s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
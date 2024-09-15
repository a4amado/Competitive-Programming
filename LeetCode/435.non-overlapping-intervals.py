#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
from typing import List

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        
        end = float('-inf')
        
        for interval in intervals:
            if interval[0] < end:
                count += 1
            else:
                end = interval[1]
        return count
    
# @lc code=end

s = Solution()

print(s.eraseOverlapIntervals(
    [[1,100],[11,22],[1,11],[2,12]]
))

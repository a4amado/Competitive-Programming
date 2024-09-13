#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        if not intervals:
            return intervals
        
        merged = []


        for interval in intervals:
            if not merged:
                merged.append(interval)     
            else:
                last = merged[len(merged) - 1]
                # if overlaping
                if interval[0] <= last[1]:
                    merged[len(merged) - 1][1] = max(interval[1], last[1])
                else:
                    merged.append(interval)

        return merged

# @lc code=end
s = Solution()
s.merge([[1,4],[2,3]])


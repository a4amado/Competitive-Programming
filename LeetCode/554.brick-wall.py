#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#
from typing import List

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        l = {}
        
        for row in wall:
            bricks_til_now = 0
            # We don't count the last brick in each row, as we don't want to consider the rightmost edge
            for brick in row[:-1]:
                bricks_til_now += brick
                if bricks_til_now in l:
                    l[bricks_til_now] += 1
                else:
                    l[bricks_til_now] = 1
        
        # If no edges are found (all rows have the same brick length), return the number of rows
        if not l:
            return len(wall)
        
        # Subtract the maximum edge count from the total number of rows to get the least bricks crossed
        return len(wall) - max(l.values())
s = Solution()
print(s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
        
# @lc code=end


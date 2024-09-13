#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

from typing import List, Set, Tuple

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        def dfs(y: int, x: int, reachable: Set[Tuple[int, int]]):
            reachable.add((y, x))
            l = getListOfNeigboursThatAreReacable(y,x,reachable)
            for y, x in l:
                dfs(y,x,reachable)

        def getListOfNeigboursThatAreReacable(y: int, x: int, reachable: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
            fl = []
            l = [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)]

            for newY, newX in l:
                if not isOutOfBound(newY, newX) and heights[newY][newX] >= heights[y][x] and (newY, newX) not in reachable:
                    fl.append([newY, newX])
            return fl
        
        def isOutOfBound(y: int, x: int) -> bool:
            maxY = len(heights)
            maxX = len(heights[0])
            if x < 0 or y < 0 or y >= maxY or x >= maxX:
                return True
            return False
        
        pacificReachable = set()
        atlanticReachable = set()

        # For Pacific Ocean
        for x in range(len(heights[0])):  # Top edge
            dfs(0, x, pacificReachable)

        for y in range(len(heights)):  # Left edge
            dfs(y, 0, pacificReachable)

        # For Atlantic Ocean
        for x in range(len(heights[0])):  # Bottom edge
            dfs(len(heights) - 1, x, atlanticReachable)

        for y in range(len(heights)):  # Right edge
            dfs(y, len(heights[0]) - 1, atlanticReachable)
        return [list(cell) for cell in pacificReachable & atlanticReachable]

# @lc code=end
 
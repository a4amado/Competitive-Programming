#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#
from itertools import groupby
# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        direction = { "N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1) }

        position = (0,0)
        previuis = set([(0,0)])

        for dir in path:
            dy, dx = direction[dir]
            position = ( position[0] + dy, position[1] + dx )
            if position in previuis: return True
            previuis.add(position)
        

        return False

# @lc code=end

sol = Solution()
print(sol.isPathCrossing("NNSWWEWSSESSWENNW"))


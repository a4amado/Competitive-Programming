#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

from typing import *

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        mst = []
        
        ranks = {idx: 0 for idx in range(1,len(isConnected) + 1)}
        parents = {idx: idx for idx in range(1,len(isConnected) + 1)}

        def find(x: int):
            if parents[x] != x:
                parents[x] = find(parents[x])

            return parents[x]
        
        def union(x: int, y: int):
            x_parent = find(x)
            y_parent = find(y)

            if x_parent == y_parent:return
            if ranks[x_parent] > ranks[y_parent]:
                parents[y_parent] = x_parent
            elif ranks[x_parent] < ranks[y_parent]:
                parents[x_parent] = y_parent
            else:
                parents[x_parent] = y_parent
                ranks[x_parent] += 1
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i+1, j+1)
        return len([x for x,v in parents.items() if x == v])

# @lc code=end

qq = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

s = Solution()
print(s.findCircleNum(qq))
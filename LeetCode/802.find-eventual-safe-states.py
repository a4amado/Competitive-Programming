#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

from typing import *

# @lc code=start

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]):
        memo = {}
        
        def dfs(idx: int, memo: True):
            if idx in memo: return memo[idx]
            memo[idx] = False

            isSafe = True
            for i in graph[idx]:
                isSafe = isSafe and dfs(i, memo)
            memo[idx] = isSafe

            return memo[idx]
        for i in range(len(graph)):
            dfs(i ,memo)
        return [k for k, v in memo.items() if v].sort()
        


        
        
# @lc code=end

s = Solution()

print( s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))


# 5,4,6
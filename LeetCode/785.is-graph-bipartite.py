#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

from typing import *

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # find if all the cycles in the graph are even length
        def dfs(idx: int, count:int, parent: int, memo: Dict):
            
            if idx in memo:
                # if return true then it's even
                return abs(memo[idx] - count) % 2 == 0

            memo[idx] = count
            
            for nei in graph[idx]:
                if nei == parent: continue
                if not dfs(nei,count +1, idx, memo):
                    return False
            
            return True
        memo = {}
        for idx in range(len(graph)):
            if idx not in memo:
                if not dfs(idx,0, -1, memo):
                    return False
        return True
    

# @lc code=end

s = Solution()


print(
    s.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
)

print(
    s.isBipartite(
        [[1,3],[0,2],[1,3],[0,2]]
    )
)
#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

from typing import List
# @lc code=start
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # intialize adjaceny list
        adjs = [[] for x in range(n)]
        
        complete = 0

        # create adjaceny list
        for edge in edges:
            adjs[edge[0]].append(edge[1])
            adjs[edge[1]].append(edge[0])
        
        visited = [False] * n

        def dfs(idx: int, chain: set):
            if visited[idx]:
                return False
            visited[idx] = True        
            chain.add(idx)
            
            for n in adjs[idx]:
                dfs(n, chain)

            return chain

        for idx in range(len(adjs)):
            if not visited[idx]:
                chain: set[int] = dfs(idx, set()) 

                is_compelete = True
                n = len(chain) - 1
                for item in chain:
                    number_of_n = len(adjs[item])
                    if n != number_of_n:
                        is_compelete = False
                if is_compelete:
                    complete += 1

        return complete
            

        
                        


        
        

# @lc code=end


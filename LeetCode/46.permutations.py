#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List,Dict

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        finaList = []
        visited = {}
        def dfs(curr: List[int], visited: Dict, final: List[List[int]]):
            if len(curr) == len(nums):
                final.append(curr.copy())
                return
            
            for i in nums:
                if i not in visited:
                    visited[i] = True
                    curr.append(i)
                    dfs(curr, visited, final)            
                    del visited[i]
                    curr.pop()
        dfs([], visited, finaList)
        return finaList

s = Solution()
s.permute([1,2,3])
s.permute([1,0])
s.permute([1])

                    

# @lc code=end


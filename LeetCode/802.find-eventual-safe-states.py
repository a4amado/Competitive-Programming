#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph ):
        n = len(graph)
        safe = {}
        res = []    



        def dfs(i):
            if i in safe:
                return safe[i]
            
            safe[i] = False
            

            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            safe[i]= True
            return True

            


        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
# @lc code=end

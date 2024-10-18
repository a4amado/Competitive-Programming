#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

from typing import *

# @lc code=start
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # all paris shortes path
        matrix = [
            [
                False for _ in range(numCourses)
            ] for _ in range(numCourses)
        ]
        for u, v in prerequisites:
            matrix[u][v] = True


        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        res = [
            matrix[i][j] for i, j in queries
        ]
        return res
            



        
        
# @lc code=end

numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]

s = Solution()
print(s.checkIfPrerequisite(numCourses, prerequisites, queries))

numCourses = 2
prerequisites = []
queries = [[1,0],[0,1]]
print(s.checkIfPrerequisite(numCourses, prerequisites, queries))

numCourses = 4
prerequisites = [[2,3],[2,1],[0,3],[0,1]]
queries = [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]
print(s.checkIfPrerequisite(numCourses, prerequisites, queries))



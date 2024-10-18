# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize the adjacency matrix
        matrix = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        
        # Set direct prerequisites
        for u, v in prerequisites:
            matrix[u][v] = True
        
        # Floyd-Warshall algorithm
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        
        # Check queries
        return [matrix[i][j] for i, j in queries]
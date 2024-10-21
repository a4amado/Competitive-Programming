from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(row: int, col: int) -> int:
            if (row, col) in memo:
                return memo[(row, col)]

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            max_length = 1

            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                if 0 <= new_row < m and 0 <= new_col < n and matrix[new_row][new_col] > matrix[row][col]:
                    max_length = max(max_length, 1 + dfs(new_row, new_col))

            memo[(row, col)] = max_length
            return max_length

        return max(dfs(i, j) for i in range(m) for j in range(n))

# @lc code=end

sol = Solution()
# print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(sol.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(sol.longestIncreasingPath([[7,8,9],[9,7,6],[7,2,3]]))




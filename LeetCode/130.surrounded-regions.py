#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

from typing import *

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(row:int, col:int, visited: Dict):
            if not (0 <= row < len(board) and 0<= col < len(board[0])):return
            if (row, col) in visited: return
            visited[(row, col)] = True
            if board[row][col] == "O":
                board[row][col] = "#"
            else: return
            dfs(row +1, col, visited)
            dfs(row -1, col, visited)
            dfs(row, col +1, visited)
            dfs(row, col -1, visited)
        # top
        for i in range(len(board[0])):
            if board[0][i] == "O":
                dfs(0, i, {})

        for i in range(len(board[0])):
            if board[-1][i] == "O":
                dfs(len(board) -1, i, {})


        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0, {})

        for i in range(len(board)):
            if board[i][-1] == "O":
                dfs(i, len(board[0]) -1, {})
 

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "#":
                    board[i][j] = "O"
                

s = Solution()

sssssssssss = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]] #[["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]]
for i in sssssssssss:
    print(i)
print("--------------------------------------------------")
s.solve(sssssssssss)
for i in sssssssssss:
    print(i)

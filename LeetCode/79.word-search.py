#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

from typing import List, Set


# @lc code=start

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Find all indices of the first char
        
        visited = [[False for _ in range(len(board[0]))] for i in range(len(board))]
        

        def dfs(idx: int, x: int, y: int):
            if idx == len(word):
                return True
            
            # is out of bound            
            if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board) or visited[y][x]:
                return False

            
            
            if board[y][x] != word[idx]:
                return False

            visited[y][x] = True
            
            
            
            found_next =   dfs(idx + 1, x + 1, y) or dfs(idx + 1, x - 1, y) or dfs(idx + 1, x , y + 1) or dfs(idx + 1, x , y - 1)
    
            visited[y][x] = False
            return found_next

        
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if col == word[0]:
                    if dfs(0, x, y):
                        return True
        return False



# @lc code=end

s = Solution()
print(s.exist([["A","B","C","D"],["S","A","A","T"],["A","C","A","E"]], "CAT"))

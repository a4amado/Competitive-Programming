#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

from typing import List


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        carry = 0

        def move(l: List[List[int]]):
            if not l:
                return
            
            nonlocal carry  # Declare carry as nonlocal to modify it
            
            y, x = l[0][0], l[0][1]
            
            matrix[y][x], carry =  carry , matrix[y][x]

            move(l[1:])
      

        for y in range(len(matrix)):
            for x in range(y, (len(matrix) - 1) - y):
                    # 3 - 1 = 2
                l = len(matrix) - 1 - y
                
                one = [y, x]
                two = [x, l]
                three = [l, l - x + y]
                four = [l - x + y, y]
        
                carry = matrix[y][x]
                
                l = [two, three, four, one]
                
                move(l)
            


# @lc code=end

s = Solution()
ll = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(ll)
for i in ll:
    print(i)

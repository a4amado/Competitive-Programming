#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        terminate = False
        def heighOfATree(node: Optional[TreeNode]) -> int:
            nonlocal terminate
            if not node :
                return 0
            

            left = 1 + heighOfATree(node.left)
            if terminate:
                return 0
            right = 1 + heighOfATree(node.right)
            
            if abs(left - right) > 1:
                terminate = True
                return 0
            return 1 +  max(left, right)
        
        heighOfATree(root)

        if terminate:
            return False
        return True


# @lc code=end


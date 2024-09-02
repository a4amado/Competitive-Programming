#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.switch(root)
        return root
    def switch(self, root: Optional[TreeNode]):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.switch(root.right)
        self.switch(root.left)
# @lc code=end


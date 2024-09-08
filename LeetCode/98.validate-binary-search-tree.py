#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
from typing import Optional, Literal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low=float("-inf"), high=float("inf")):
            if not node:
                return True
            
            val = node.val
            if val >= high or val <= low:
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)


# @lc code=end


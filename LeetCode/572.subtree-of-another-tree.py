#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
from typing import *


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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node: Optional[TreeNode]):
            if not node:
                return "null"
            # Using string formatting with unique markers to avoid false matches
            return f"#{node.val}#{serialize(node.left)}#{serialize(node.right)}"
            
        def getSubtrees(node: Optional[TreeNode], subtrees: set):
            if not node:
                return "null"
            # Create serialization for current subtree
            curr = f"#{node.val}#{getSubtrees(node.left, subtrees)}#{getSubtrees(node.right, subtrees)}"
            # Add current subtree to set
            subtrees.add(curr)
            return curr

        # Get all possible subtree serializations from root
        subtrees = set()
        getSubtrees(root, subtrees)
        
        # Check if subRoot serialization exists in our subtrees
        target = serialize(subRoot)
        return target in subtrees

        

        
# @lc code=end


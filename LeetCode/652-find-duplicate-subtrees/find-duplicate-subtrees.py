#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
from typing import *

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Helper function to check if two trees are the same (not needed in final solution)

        # Main solution using subtree serialization
        subtrees = defaultdict(int)  # Hash map to store the count of each subtree encoding
        result = []    # List to store root nodes of duplicate subtrees

        def encode(node):
            if not node:
                return "#"  # Use # to represent null nodes
            
            # Create unique encoding for this subtree
            # Format: val(left_subtree)(right_subtree)
            encoding = f"{node.val}({encode(node.left)})({encode(node.right)})"
            
            # Track the count of this encoding
            subtrees[encoding] += 1
            
            # If we've seen this subtree exactly twice, add it to result
            if subtrees[encoding] == 2:
                result.append(node)
                
            return encoding

        encode(root)  # Start the encoding process from root
        return result
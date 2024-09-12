#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

from typing import Optional, List


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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q: List[Optional[TreeNode]] = [root]
        final = []
        
        while q:

            curr_level = []
            
            for i in q:
                curr_level.append(i.val)
            
            if curr_level:
                final.append(curr_level)
            
            next_level = []

            for item in q:
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)

            q = next_level
            
            
            
            
        
        return final

# @lc code=end


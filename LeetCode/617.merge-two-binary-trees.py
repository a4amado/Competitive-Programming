#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        if not root2: return root1
        if not root1 and not root2: return

        def merge(nood1: Optional[TreeNode], nood2: Optional[TreeNode]):
            if not nood1 and not nood2: return

            new_node = TreeNode()

            if nood1 and nood2:
                new_node.val = nood1.val + nood2.val
            
            if not nood2:
                new_node.val = nood1.val
            elif not nood1:
                new_node.val = nood2.val

            merge_left = merge(nood1.left if nood1 else None, nood2.left if nood2 else None)

            if merge_left:
                new_node.left = merge_left

            merge_right = merge(nood1.right if nood1 else None, nood2.right if nood2 else None)

            if merge_right:
                new_node.right = merge_right
            
            return new_node
        
        return merge(root1, root2)


# @lc code=end


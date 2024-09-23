#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
from typing import List, Optional

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q: List[TreeNode] = []
        view: List[int] = []
        # append level 1 to queqe
        q.append(root)
        while q:
            levelInOrder = []
            newQ = []
            for node in q:
                if node:
                    levelInOrder.append(node.val)
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)

            view.append([levelInOrder[-1]])
            q = newQ
        return [x[-1] for x in view]
            
            
# @lc code=end


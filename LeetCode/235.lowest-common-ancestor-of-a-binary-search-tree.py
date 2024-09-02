#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

from typing import Optional, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        q_a = []
        p_a = []
        self.look(root, p.val, p_a)
        self.look(root, q.val, q_a)
        if len(q_a) == 0:
            q_a.append(root.val)
        if len(p_a) == 0:
            p_a.append(root.val)
        
        # Find the lowest common ancestor
        lowest = sorted(list(set(p_a) & set(q_a)))[0]
        # Return the TreeNode corresponding to the LCA
        return self.find_node(root, p_a[lowest])
    
    def look(self, root: Optional[TreeNode], f: int, l: List[int]) -> bool:
        if not root:
            return False
        l.append(root.val)
        if f == root.val:
            return True
        left = self.look(root.left, f, l)
        right = self.look(root.right, f, l)
        if not left and not right:
            l.pop()
        return left or right
    
    def find_node(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        left = self.find_node(root.left, val)
        if left:
            return left
        return self.find_node(root.right, val)

        
# @lc code=end


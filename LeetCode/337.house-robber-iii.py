#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
from typing import *

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node, memo):
            if not node:
                return 0
                
            if node in memo:
                return memo[node]
            
            # Take node value
            take = node.val
            
            # If taking this node, skip its children but can take grandchildren
            if node.left:
                take += dfs(node.left.left, memo) + dfs(node.left.right, memo)
            if node.right:
                take += dfs(node.right.left, memo) + dfs(node.right.right, memo)
                
            # Don't take node value, can take children
            noTake = dfs(node.left, memo) + dfs(node.right, memo)
            
            memo[node] = max(take, noTake)
            return memo[node]
            
        return dfs(root, {})
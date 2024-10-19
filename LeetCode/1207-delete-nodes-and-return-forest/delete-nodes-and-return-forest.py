# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        to_delete_set = set(to_delete)
        forest = []
        
        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return None
            
            # Check if the current node should become a new root
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            
            # Recurse on left and right children
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            
            # If the current node is deleted, return None to "cut" it from the tree
            return None if root_deleted else node
        
        dfs(root, True)
        return forest
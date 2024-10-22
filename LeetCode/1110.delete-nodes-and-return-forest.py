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
        
        to_delete_set = set(to_delete)  # Convert the list to a set for O(1) lookups
        forest = []

        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return None
            
            # Check if the current node is to be deleted
            root_deleted = node.val in to_delete_set
            
            # If the node is not deleted and is a root (either original root or new root), add it to the forest
            if is_root and not root_deleted:
                forest.append(node)
            
            # Recur on the left and right children
            node.left = dfs(node.left, root_deleted)   # If the current node is deleted, its children become new roots
            node.right = dfs(node.right, root_deleted) # If the current node is deleted, its children become new roots
            
            # Return None if the node is deleted, meaning it is removed from the tree
            return None if root_deleted else node
        
        # Start DFS with the root, considering it as the root of the tree
        dfs(root, True)
        
        return forest

# @lc code=end


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values, index=0):
    if index >= len(values) or values[index] is None:
        return None
    node = TreeNode(values[index])
    node.left = build_tree(values, 2 * index + 1)
    node.right = build_tree(values, 2 * index + 2)
    return node

# Input values
root_values = [1, 2, 3, 4, 5, 6, 7]

# Build tree from list
root = build_tree(root_values)
s = Solution()
# print(
#     s.delNodes(root, [3,5])
# )

def build_tree(values, index=0):
    if index >= len(values) or values[index] is None:
        return None
    node = TreeNode(values[index])
    node.left = build_tree(values, 2 * index + 1)
    node.right = build_tree(values, 2 * index + 2)
    return node

# Input values with some None entries
root_values = [1, 2, 3, None, None, None, 4]

# Build tree from list
root = build_tree(root_values)

print(
    s.delNodes(root, [2,1])
)
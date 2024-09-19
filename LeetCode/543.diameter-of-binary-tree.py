from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def calculate_depth(node: Optional[TreeNode]):
            nonlocal diameter
            if not node:
                return 0

            left_depth = calculate_depth(node.left) 
            right_depth = calculate_depth(node.right) 

            # Calculate diameter through the current node
            diameter = max(diameter, left_depth + right_depth + 1)

            # Return the maximum depth of the subtree rooted at the current node
            return max(left_depth, right_depth) + 1

        calculate_depth(root)
        return diameter - 1

# Input: root = [1,2,3,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = Solution().diameterOfBinaryTree(root)
print(result)  # Output: 3
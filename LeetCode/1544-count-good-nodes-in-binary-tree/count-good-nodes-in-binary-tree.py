# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        def good_nodes(node: Optional[TreeNode], maxTilNow: int):
            if not node: return 0

            countFromHere = 1 if node.val >= maxTilNow else 0

            right = good_nodes(node.right, max(node.val, maxTilNow))
            left = good_nodes(node.left, max(node.val, maxTilNow))

            return countFromHere + right + left
        return good_nodes(root, float('-inf'))
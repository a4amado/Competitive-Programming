# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        
        def preorderfn(node: Optional[TreeNode], l: List[int]):
            if not node:return
            
            l.append(node.val)
            preorderfn(node.left, l)
            preorderfn(node.right, l)
        preorderfn(root, preorder)

        return preorder
        
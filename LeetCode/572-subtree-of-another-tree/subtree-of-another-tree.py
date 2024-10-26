class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node: Optional[TreeNode]):
            if not node:
                return "null"
            # Using string formatting with unique markers to avoid false matches
            return f"#{node.val}#{serialize(node.left)}#{serialize(node.right)}"
            
        def getSubtrees(node: Optional[TreeNode], subtrees: set):
            if not node:
                return "null"
            # Create serialization for current subtree
            curr = f"#{node.val}#{getSubtrees(node.left, subtrees)}#{getSubtrees(node.right, subtrees)}"
            # Add current subtree to set
            subtrees.add(curr)
            return curr

        # Get all possible subtree serializations from root
        subtrees = set()
        getSubtrees(root, subtrees)
        
        # Check if subRoot serialization exists in our subtrees
        target = serialize(subRoot)
        return target in subtrees
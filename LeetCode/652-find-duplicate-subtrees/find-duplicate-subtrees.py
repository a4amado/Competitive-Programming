class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Helper function to check if two trees are the same (not needed in final solution)
        def is_same_tree(node: Optional[TreeNode], other_node: Optional[TreeNode]):
            if not node and not other_node: return True
            if not node or not other_node: return False
            if node.val != other_node.val: return False

            is_left = is_same_tree(node.left, other_node.left)
            is_right = is_same_tree(node.right, other_node.right)

            return is_left and is_right
        
        # Main solution using subtree serialization
        subtrees = {}  # Hash map to store the count of each subtree encoding
        result = []    # List to store root nodes of duplicate subtrees

        def encode(node):
            if not node:
                return "#"  # Use # to represent null nodes
            
            # Create unique encoding for this subtree
            # Format: val(left_subtree)(right_subtree)
            encoding = f"{node.val}({encode(node.left)})({encode(node.right)})"
            
            # Track the count of this encoding
            subtrees[encoding] = subtrees.get(encoding, 0) + 1
            
            # If we've seen this subtree exactly twice, add it to result
            if subtrees[encoding] == 2:
                result.append(node)
                
            return encoding

        encode(root)  # Start the encoding process from root
        return result
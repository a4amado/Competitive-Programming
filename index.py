from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        q_a = []
        p_a = []
        self.look(root, p.val, p_a)
        self.look(root, q.val, q_a)
        if len(q_a) == 0:
            q_a.append(root.val)
        if len(p_a) == 0:
            p_a.append(root.val)
        
        print("Path to q:", q_a)
        print("Path to p:", p_a)
        
        
        return self.find_node(root, lca_val)

    def look(self, root: TreeNode, f: int, l: List[int]) -> bool:
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

    def find_node(self, node, value):
        if not node:
            return None
        if node.val == value:
            return node
        left = self.find_node(node.left, value)
        if left:
            return left
        return self.find_node(node.right, value)

# Create the tree
def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# Test the code
if __name__ == "__main__":
    # Create the tree
    values = [6,2,8,0,4,7,9,None,None,3,5]
    root = create_tree(values)

    # Create Solution instance
    solution = Solution()

    # Test with p = 2 and q = 8
    p = TreeNode(2)
    q = TreeNode(8)

    # Call the method
    result = solution.lowestCommonAncestor(root, p, q)
    print("Lowest Common Ancestor:", result.val if result else None)
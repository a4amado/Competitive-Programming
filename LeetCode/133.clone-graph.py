#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return node
    

        alreadyCreatedNodes = {}

        def copy(nodeToCopy: Node):
            if nodeToCopy.val in alreadyCreatedNodes:
                return alreadyCreatedNodes[nodeToCopy.val]

            root = Node(nodeToCopy.val)
            alreadyCreatedNodes[nodeToCopy.val] = root    
            
            for nei in nodeToCopy.neighbors:
                root.neighbors.append(copy(nei))
            
            return root
        return copy(node)
            

        
        
# @lc code=end


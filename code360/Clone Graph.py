from os import *
from sys import *
from collections import *
from math import *

# Class for graph node is as follows:
class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()

from typing import *

def cloneGraph(node:Optional[graphNode]) -> Optional[graphNode]:
    if not node:
        return None
    
    def clone(root:graphNode, visited: Dict[int, graphNode]) -> graphNode:
        if root.data in visited: return visited[root.data]

        newNode = graphNode(root.data)
        visited[root.data] = newNode

        # clone children
        for nei in root.neighbours:
            newNei = clone(nei, visited)
            newNode.neighbours.append(newNei)
        
        return newNode
    
    return clone(node, {})

def cloneGraph(node: Optional[graphNode]) -> Optional[graphNode]:
    if not node:
        return None
    
    def clone(root: graphNode, visited: Dict[int, graphNode]) -> graphNode:
        if root.data in visited:
            return visited[root.data]
        
        # Create a new node for the current root
        newNode = graphNode(root.data)
        visited[root.data] = newNode
        
        # Recursively clone all neighbours
        for nei in root.neighbours:
            newNei = clone(nei, visited)
            newNode.neighbours.append(newNei)
        
        return newNode

    return clone(node, {})

def cloneGraph(node: Optional[graphNode]) -> Optional[graphNode]:
    if not node:
        return None
    
    def clone(root: graphNode, visited: Dict[int, graphNode]) -> graphNode:
        if root.data in visited:
            return visited[root.data]
        
        # Create a new node for the current root
        newNode = graphNode(root.data)
        visited[root.data] = newNode
        
        # Recursively clone all neighbours
        for nei in root.neighbours:
            newNei = clone(nei, visited)
            newNode.neighbours.append(newNei)
        
        return newNode

    return clone(node, {})

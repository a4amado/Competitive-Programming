from os import *
from sys import *
from collections import *
from math import *
from bisect import bisect_left, bisect_right

'''
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

# Function to perform in-order traversal and store nodes in a sorted list
def in_order_traversal(root, sorted_nodes):
    if root is None:
        return
    in_order_traversal(root.left, sorted_nodes)
    sorted_nodes.append(root.data)
    in_order_traversal(root.right, sorted_nodes)

def bstQueries(root, q, queries):
    # Step 1: Perform in-order traversal to get sorted node values
    sorted_nodes = []
    in_order_traversal(root, sorted_nodes)
    
    results = []
    
    # Step 2: For each query, use binary search to find the range [L, R]
    for L, R in queries:
        # Find the leftmost index where sorted_nodes[index] >= L
        left_idx = bisect_left(sorted_nodes, L)
        # Find the rightmost index where sorted_nodes[index] <= R
        right_idx = bisect_right(sorted_nodes, R)
        
        # The number of nodes in the range is the difference between the indices
        results.append(right_idx - left_idx)
    
    return results

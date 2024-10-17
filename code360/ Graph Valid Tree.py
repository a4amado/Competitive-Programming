from os import *
from sys import *
from collections import *
from math import *

from typing import List

def checkgraph(edges: List[List[int]], n: int, m: int):
    if len(edges) != n -1: return False

    parents = {idx:idx for idx in range(n)}
    ranks = {idx:0 for idx in range(n)}

    def find(x: int):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def uniuon(x: int, y: int):
        parent_x = find(x)
        parent_y = find(y)

        if parent_x == parent_y: return

        if ranks[parent_x] > ranks[parent_y]:
            parents[parent_y] = parent_x
        elif ranks[parent_x] < ranks[parent_y]:
            parents[parent_x] = parent_y
        else:
            parents[parent_x] = parent_y
            ranks[parent_y] += 1
        

    for u,v in edges:
        uniuon(u, v)

    # count how many components we got
    count = 0
    for item, parent in parents.items():
        if item == parent:
            count += 1
    
    if count != 1: return False

    return True
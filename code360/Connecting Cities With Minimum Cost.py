from os import *
from sys import *
from collections import *
from math import *
from typing import *

class UnionFind():
    def __init__(self, n: int) -> None:
        self.ranks = { idx + 1: 0 for idx in range(n) }
        self.parents = { idx + 1: idx + 1 for idx in range(n) }

    def find(self, x: int):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x: int, y: int):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:return False

        if self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = parent_x
        elif self.ranks[parent_x] < self.ranks[parent_y]:
            self.parents[parent_x] = parent_y
        else:
            self.parents[parent_x] = parent_y
            self.ranks[parent_y] += 1
        return True


def getMinimumCost(n: int, m: int, connections:List[List[int]]):
        # adjs = {idx + 1: set() for idx in range(n + 1)}
        # for u, v, w in connections:
        #     adjs[u].add((v, w))
        #     adjs[v].add((u, w))
        union = UnionFind(n)
        cost = 0
        connections.sort(key=lambda x:x[-1])
        for u,v,w in connections:
            if union.union(u, v):
                cost += w
        # find if any children are lonley
        parents = 0
        for i, v  in union.parents.items():
            if i == v :
                parents += 1
        if parents > 1: return -1

        return cost



        



n = 5
m = 6
connections = [[1,2,6], [2,3,5], [3,4,4], [1,4,1], [1,3,2], [3,5,3]]

print(getMinimumCost(n, m , connections))

n = 3
m = 1
connections = [[1, 2, 4]]

print(getMinimumCost(n, m , connections))
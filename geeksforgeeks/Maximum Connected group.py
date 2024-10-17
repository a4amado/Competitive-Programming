from typing import List, Tuple
import heapq

class Solution:
    def MaxConnection(self, grid : List[List[int]]) -> int:
        
        

        parents = {}
        valOfCells = {}

        def calcTheValOfCell(row: int, col: int):
            return (row * len(grid)) + col
        
        def count(row:int, col: int, all: List[int], parent: int):
            # DFS a node get all the 1's connected to it
            if row < 0 or col <0: return
            if row >= len(grid) or col >= len(grid): return
            if grid[row][col] == 0:return
            cellVal = calcTheValOfCell(row, col)
            if cellVal in visited: return
            visited[cellVal] = True
            
            all.append(cellVal)
            parents[cellVal] = parent

            count(row + 1, col, all, parent)
            count(row - 1, col, all, parent)
            count(row, col + 1, all, parent)
            count(row, col - 1, all, parent)


        visited = {}
        for row in range(len(grid)):
            for col in range(len(grid)):
                key = calcTheValOfCell(row, col)
                if key in visited: continue
                if grid[row][col] == 0: continue
                listOfConnectedCells = []
                count(row, col,listOfConnectedCells, key)
                # fill all these cells with the size of there group
                for i in listOfConnectedCells:
                    valOfCells[i] = len(listOfConnectedCells)


        def isOutOfBound(row: int, col: int):
            if row < 0: return True
            if col < 0: return True
            if row >= len(grid): return True
            if col >= len(grid): return True
            if grid[row][col] == 0: return True

            return False
        
        valOdBiggestTilNow = float('-inf')

        for row in range(len(grid)):
            for col in range(len(grid)):
                curr = grid[row][col]
                if curr == 1: continue

                allFour = [(row + 1, col),(row - 1, col),(row, col + 1),(row, col - 1)]

                # remove all outofbound
                 
                allInBound = [
                    (newRow, newCol) for newRow, newCol in allFour if not isOutOfBound(newRow,newCol)
                ]

                allUniqie = {}
                for newRow, newCol in allInBound:
                    key = parents[calcTheValOfCell(newRow, newCol)]
                    if key not in allUniqie:
                        allUniqie[key] = (newRow, newCol)

                sumAll = sum([
                    valOfCells[calcTheValOfCell(newRow, newCol)] for newRow, newCol in allUniqie.values()
                ])
                if sumAll >= valOdBiggestTilNow:
                    valOdBiggestTilNow = sumAll
        return valOdBiggestTilNow + 1
                
graph = [[1, 1],
             [0, 1]]

s = Solution()        
print(s.MaxConnection(graph))         
graph = [
[1, 0, 1],
[1, 0, 1],
[1, 0, 1]
]





from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.size = [1] * size  # To store the size of each component
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Helper function to calculate the unique cell value from (row, col)
        def calcTheValOfCell(row: int, col: int) -> int:
            return row * n + col
        
        # Initialize UnionFind for n * n cells
        uf = UnionFind(n * n)
        
        # Step 1: Union all adjacent 1's
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    cellVal = calcTheValOfCell(row, col)
                    
                    # Check 4 neighbors (up, down, left, right)
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dr, dc in directions:
                        newRow, newCol = row + dr, col + dc
                        if 0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 1:
                            neighborVal = calcTheValOfCell(newRow, newCol)
                            uf.union(cellVal, neighborVal)
        
        # Step 2: Find the maximum connection by turning a 0 into a 1
        max_connection = max(uf.size)  # Max component size already present (all 1's connected)
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    # We are considering turning this 0 into a 1
                    unique_parents = set()
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    
                    for dr, dc in directions:
                        newRow, newCol = row + dr, col + dc
                        if 0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 1:
                            neighborVal = calcTheValOfCell(newRow, newCol)
                            unique_parents.add(uf.find(neighborVal))
                    
                    # Sum the sizes of the unique neighboring components
                    total_size = 1  # Adding the new cell itself
                    for parent in unique_parents:
                        total_size += uf.get_size(parent)
                    
                    # Track the maximum connected size
                    max_connection = max(max_connection, total_size)
        
        return max_connection

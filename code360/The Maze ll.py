from heapq import heappop, heappush
from typing import List

def isOutOfBound(row: int, col: int, maxRow: int, maxCol: int):
    return not (0 <= row < maxRow and 0 <= col < maxCol)

def mazeRunner(n: int, m: int, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = []
    visited = [[float('inf')] * m for _ in range(n)]
    
    # Initialize heap with start position in all directions
    for dy, dx in directions:
        newRow, newCol = start[0] + dy, start[1] + dx
        if not isOutOfBound(newRow, newCol, n, m) and maze[newRow][newCol] != 1:
            heappush(heap, (1, newRow, newCol, dy, dx))
    
    visited[start[0]][start[1]] = 0
    
    while heap:
        w, row, col, dy, dx = heappop(heap)
        
        if visited[row][col] <= w: 
            continue  # Skip if a better path to (row, col) has already been found
        
        visited[row][col] = w
        
        # Early exit when the destination is reached
        if [row, col] == destination:
            return w
        
        # Move in the current direction until hitting a wall or boundary
        newRow, newCol = row + dy, col + dx
        
        if isOutOfBound(newRow, newCol, n, m) or maze[newRow][newCol] == 1:
            # If direction is blocked, try other directions
            for newDy, newDx in directions:
                adjRow, adjCol = row + newDy, col + newDx
                if not isOutOfBound(adjRow, adjCol, n, m) and maze[adjRow][adjCol] != 1:
                    heappush(heap, (w + 1, adjRow, adjCol, newDy, newDx))
        else:
            heappush(heap, (w + 1, newRow, newCol, dy, dx))
    
    return -1  # Return -1 if there's no path to the destination

# Test Cases
N = 3
M = 3
Maze = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0]
]
Start = [0, 0]
Destination = [2, 1]
print(mazeRunner(N, M, Maze, Start, Destination))  # Expected output: 4

N = 3
M = 4
Maze = [[1, 0, 1, 0], [0, 0, 0, 1], [0, 0, 1, 1]]
Start = [2, 1]
Destination = [1, 2]
print(mazeRunner(N, M, Maze, Start, Destination))  # Expected output: 3

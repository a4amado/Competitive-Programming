from typing import List

def numOfIslandsII(n: int, m: int, q: List[List[int]]) -> List[int]:
    def calcCellVal(row: int, col: int) -> int:
        return (row * m) + col  # Changed n to m
    
    parent = {
        calcCellVal(row, col): float('inf') for col in range(m) for row in range(n)
    }

    def find(val: int) -> int:
        if parent[val] == float('inf'):
            return float('inf')
        if parent[val] != val:
            parent[val] = find(parent[val])
        return parent[val]
    
    def union(val1: int, val2: int):
        root1, root2 = find(val1), find(val2)
        if root1 != float('inf') and root2 != float('inf'):
            parent[root2] = root1
    
    count = 0
    result = []
    visited = set()
    
    for row, col in q:
        cell_val = calcCellVal(row, col)
        if cell_val in visited:
            result.append(count)
            continue
        
        visited.add(cell_val)
        parent[cell_val] = cell_val
        count += 1

        nextDoorNodes = [(row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)]
        for newRow, newCol in nextDoorNodes:
            if 0 <= newRow < n and 0 <= newCol < m:
                newCellVal = calcCellVal(newRow, newCol)
                if find(newCellVal) != float('inf'):
                    if find(cell_val) != find(newCellVal):
                        count -= 1
                        union(cell_val, newCellVal)

        result.append(count)
    
    return result
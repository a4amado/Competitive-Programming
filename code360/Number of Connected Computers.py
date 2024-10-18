from typing import List, Literal, Set

def totalConnectedComp(arr: List[List[int]], n: int, m: int):
    def cacl(row: int, col: int):
        return row * len(arr) + col
    lowerBoundry = 0
    upperBoundrey = len(arr) * len(arr[0])

    def all(row: int, col: int, direction: Literal["up", "down", "left", "right"], visited: Set):
        key = cacl(row, col)
        if key < lowerBoundry: return 0
        if key >= upperBoundrey: return 0
        if key in visited: return 0
        
        visited.add(key)

        sumAll = 0
        if arr[row][col] == 1:
            sumAll = 1
            sumAll += all(row + 1, col, "down", visited)
            sumAll += all(row - 1, col, "up", visited)
            sumAll += all(row, col + 1, "right", visited)
            sumAll += all(row, col - 1, "left", visited)
        else:
            if direction == "down":
                sumAll += all(row + 1, col, direction, visited)
            elif direction == "up":
                sumAll += all(row - 1, col, direction, visited)
            elif direction == "right":
                sumAll += all(row, col + 1, direction, visited)
            elif direction == "left":
                sumAll += all(row, col - 1, direction, visited)
        return sumAll
    
    visited = set()
    total = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if cacl(row, col) in visited: continue
            if arr[row][col] == 0: continue
            sumD = all(row, col, "up", visited)
            if sumD > 1:
                total += sumD
    return total

matrix = [[1,1,0,0],
[0,0,1,0],
[0,0,0,1],
[0,0,0,1]]

print(totalConnectedComp(matrix,0,0))
matrix = [[1,0],
[1,1]]
print(totalConnectedComp(matrix,0,0))

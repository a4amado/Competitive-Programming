class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid1), len(grid1[0])
        
        def getIsland(row: int, col: int, grid: List[List[int]], island: set) -> None:
            # Check bounds and water cells
            if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] == 0:
                return

            # Add current cell to island
            island.add((row, col))
            # Mark as visited
            grid[row][col] = 0
            
            # Explore all 4 directions
            for dy, dx in directions:
                getIsland(row + dy, col + dx, grid, island)
        
        # Make a copy of grid2 since we'll modify it
        grid2_copy = [row[:] for row in grid2]
        sub_islands = 0
        
        # Iterate through grid2
        for row in range(rows):
            for col in range(cols):
                if grid2_copy[row][col] == grid2_copy[row][col] == 1:
                    # Get the island from grid2
                    grid2_island = set()
                    getIsland(row, col, grid2_copy, grid2_island)
                    
                    # Check if this island is a sub-island
                    is_sub_island = True
                    for y, x in grid2_island:
                        if grid1[y][x] == 0:
                            is_sub_island = False
                            break
                    
                    if is_sub_island:
                        sub_islands += 1
                        
        return sub_islands
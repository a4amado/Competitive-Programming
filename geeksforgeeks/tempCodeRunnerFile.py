

		
		q = deque([])
		for rowIdx, row  in enumerate(grid):
			for colIdx, col  in enumerate(row):
				if col == 1:
					q.append((0, (rowIdx, colIdx)))
				grid[rowIdx][colIdx] = 0

		visited = {}
		while q:
			(distance, (row, col)) = q.popleft()
			if (row, col) in visited: continue

			grid[row][col] = min(distance + 1, grid[row][col])


			nei = [(1,0), (-1, 0), (0,-1), (0, 1)]
			for (y, x) in nei:
				newRow = row + y
				newCol = col + x
				if newRow < 0 or newCol < 0 or newRow >= len(grid) or newCol >= len(grid[0]): continue
				q.append((distance + 1, (newRow, newCol)))
			visited[(row, col)] = True
		
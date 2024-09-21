from typing import List, Tuple

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_out_of_bound(row: int, col: int) -> bool:
            return row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])

        def is_fresh(row: int, col: int) -> bool:
            return grid[row][col] == 1

        def get_all_adjacent_fresh_oranges(row: int, col: int) -> List[Tuple[int, int]]:
            adjs = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            return [(r, c) for r, c in adjs if not is_out_of_bound(r, c) and is_fresh(r, c)]

        q: List[Tuple[int, int]] = []
        fresh = sum(row.count(1) for row in grid)
        rotten = sum(row.count(2) for row in grid)

        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                if cell == 2:
                    q.append((row_idx, col_idx))

        adjs = q.copy()
        count = 0
        while adjs:
            new_list = set()
            for i in adjs:
                new_list.update(get_all_adjacent_fresh_oranges(i[0], i[1]))
            for item in new_list:
                grid[item[0]][item[1]] = 2
                fresh -= 1

            adjs = list(new_list)
            if adjs:
                count += 1

        return -1 if fresh else count
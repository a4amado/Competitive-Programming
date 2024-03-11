/*
 * @lc app=leetcode id=463 lang=java
 *
 * [463] Island Perimeter
 */

// @lc code=start
class Solution {
    public int islandPerimeter(int[][] grid) {
        Boolean[][] visited = new Boolean[grid.length][grid[0].length];

        Integer[] n = new Integer[1];
        n[0] = 0;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {

                if (grid[row][col] == 1) {

                    this.dfs(grid, row, col, visited, n);
                    return n[0];
                } else {
                    visited[row][col] = true;

                }
            }
        }
        return 0;
    }

    private void dfs(int[][] grid, int row, int col, Boolean[][] visited, Integer[] n) {

        if (this.isOutOfBound(grid, row, col) || visited[row][col] != null || grid[row][col] == 0)
            return;
        visited[row][col] = true; // Mark the current cell as visited

        n[0] = n[0] + (4 - this.numberOfSeroundingLand(grid, row, col));

        this.dfs(grid, row + 1, col, visited, n);
        this.dfs(grid, row - 1, col, visited, n);
        this.dfs(grid, row, col - 1, visited, n);
        this.dfs(grid, row, col + 1, visited, n);

    }

    private int numberOfSeroundingLand(int[][] grid, int row, int col) {
        Integer serroundingLand = 0;
        serroundingLand = serroundingLand + (this.isOutOfBound(grid, row - 1, col) || (grid[row - 1][col] == 0) ?  0: 1);
        serroundingLand = serroundingLand + (this.isOutOfBound(grid, row + 1, col) || (grid[row + 1][col] == 0) ?  0: 1);
        serroundingLand = serroundingLand + (this.isOutOfBound(grid, row, col - 1) || (grid[row][col - 1] == 0) ?  0: 1);
        serroundingLand = serroundingLand + (this.isOutOfBound(grid, row, col + 1) || (grid[row][col + 1] == 0) ?  0: 1);
        return serroundingLand;
    }

    private boolean isOutOfBound(int[][] grid, int row, int col) {
        if (row < 0 || col < 0)
            return true;
        Integer max = grid.length - 1;
        Integer colMax = grid[0].length - 1;
        if (row > max || col > colMax)
            return true;
        return false;
    }
}

// @lc code=end

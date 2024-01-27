/*
 * @lc app=leetcode id=200 lang=java
 *
 * [200] Number of Islands
 */

import java.util.*;

// @lc code=start

class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0; // handle null or empty grid
        }

        boolean[][] visited = new boolean[grid.length][grid[0].length];

        int[] islandCount = new int[1];

        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {

                if (grid[row][col] == '1' && visited[row][col] != true) {
                    this.checkAllConnectedLand(grid, visited, row, col);
                    islandCount[0]++;
                }

            }
        }
        return islandCount[0];
    }

    private void checkAllConnectedLand(char[][] grid, boolean[][] visited, int row, int col) {
        if (isOutOfBound(grid, row, col) || visited[row][col] || grid[row][col] == '0')
            return;

        visited[row][col] = true;

        checkAllConnectedLand(grid, visited, row - 1, col);
        checkAllConnectedLand(grid, visited, row + 1, col);
        checkAllConnectedLand(grid, visited, row, col - 1);
        checkAllConnectedLand(grid, visited, row, col + 1);
    }

    private boolean isOutOfBound(char[][] grid, int row, int col) {
        return row < 0 || row >= grid.length || col < 0 || col >= grid[0].length;
    }
}

// @lc code=end

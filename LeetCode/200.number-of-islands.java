/*
 * @lc app=leetcode id=200 lang=java
 *
 * [200] Number of Islands
 */


import java.util.*;
// @lc code=start
class Solution {
    public int numIslands(char[][] grid) {
        Map<String, Boolean> visted = new HashMap<>();
        int[] n = new int[1];
        n[0] = 0;

        for (int row  = 0; row < grid.length; row++) {
            for (int col  = 0; col < grid[0].length; col++) {
                if (grid[row][col] == '1' && !visted.containsKey(row + "" + col)) {
                    n[0]++;
                    this.check_all_conected_land(grid, visted, row, col);
                } else {
                    visted.put(row +"" + col, true);
                }

            }
        }
        return n[0];
    }

    private void check_all_conected_land(char[][] grid, Map<String, Boolean> visted, int  row, int col) {
        if (this.isOutOfBound(grid, visted, row, col)) return;

        if (visted.containsKey(row +"" + col)) return;
        if (grid[row][col] == '0') return;
        
        visted.put(row +"" + col, true);

        this.check_all_conected_land(grid, visted, row - 1, col);
        this.check_all_conected_land(grid, visted, row + 1, col);
        this.check_all_conected_land(grid, visted, row, col - 1);
        this.check_all_conected_land(grid, visted, row, col + 1);
    }

    private boolean isOutOfBound(char[][] grid, Map<String, Boolean> visited, int row, int col) {
        if (row < 0 || row >= grid.length) return true;
        if (col < 0 || col >= grid[0].length) return true;
        return false;
    }
    
}
// @lc code=end



/*
 * @lc app=leetcode id=695 lang=cpp
 *
 * [695] Max Area of Island
 */
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start

class Solution
{
public:
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        if (grid.size() == 0)
            return 0;

        int y = grid.size();
        int x = y == 0 ? 0 : grid[0].size();
        vector<vector<int>> visited(y, vector<int>(x, false));
        int biggest_size = 0;
        for (int row = 0; row < y; ++row)
        {
            for (int col = 0; col < grid[row].size(); col++)
            {
                if (grid[row][col] && !visited[row][col])
                {
                    int counter = 0;
                    biggest_size = max(dfs(grid, row, col, false, visited, counter, biggest_size), biggest_size);
                }
            }
        };
        return biggest_size;
    }

    int dfs(vector<vector<int>> &grid, int row, int col, bool not_island, vector<vector<int>> &visited, int &counter, int &biggest_size)
    {
      if (isOutOfRange(grid, row, col) || grid[row][col] == 0 || visited[row][col])
        return 0;

    visited[row][col] = true;
    counter++;

    dfs(grid, row + 1, col, false, visited, counter, biggest_size);
    dfs(grid, row - 1, col, false, visited, counter, biggest_size);
    dfs(grid, row, col + 1, false, visited, counter, biggest_size);
    dfs(grid, row, col - 1, false, visited, counter, biggest_size);

    return counter;
    }

    bool isOutOfRange(vector<vector<int>> &grid, int row, int col)
    {
        if (row < 0)
            return true;
        if (col < 0)
            return true;

        if (row > grid.size() - 1)
            return true;
        if (col > grid[row].size() - 1)
            return true;

        return false;
    }
};

// @lc code=end

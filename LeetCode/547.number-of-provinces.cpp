/*
 * @lc app=leetcode id=547 lang=cpp
 *
 * [547] Number of Provinces
 */
#include <iostream>
#include <vector>

using namespace std;

// @lc code=start
#include <vector>
using namespace std;

class Solution
{
public:
    int findCircleNum(vector<vector<int>> &isConnected)
    {
        int count = 0;
        vector<bool> visited(isConnected.size(), false);

        for (int row = 0; row < isConnected.size(); row++)
        {
            if (!visited[row])
            {
                count++;
                dfs(isConnected, visited, row); // Start DFS from the unvisited node
            }
        }
        return count;
    }

    void dfs(vector<vector<int>> &isConnected, vector<bool> &visited, int node)
    {
        visited[node] = true;

        for (int col = 0; col < isConnected[node].size(); col++)
        {
            if (isConnected[node][col] && !visited[col])
            {
                dfs(isConnected, visited, col); // Recursively visit connected nodes
            }
        }
    }
};

// @lc code=end

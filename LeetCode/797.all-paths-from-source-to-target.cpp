
/*
 * @lc app=leetcode id=797 lang=cpp
 *
 * [797] All Paths From Source to Target
 */
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// @lc code=start
class Solution
{
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph)
    {
        vector<vector<int>> links;
        vector<int> path = {0};
        dfs(graph, 0, path, links);
        return links;
    }
    void dfs(vector<vector<int>> &graph, int c, vector<int>  path, vector<vector<int>> &links)
    {
        // when reach the target
        if (c == graph.size() - 1)
        {
            links.push_back(path);
            return;
        };

        for (auto neibouger : graph[c])
        {
            path.push_back(neibouger);
            dfs(graph, neibouger, path, links);
            path.pop_back();
        }
    }
};
// @lc code=end

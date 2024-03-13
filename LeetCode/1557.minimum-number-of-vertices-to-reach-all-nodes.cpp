#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

/*
 * @lc app=leetcode id=1557 lang=cpp
 *
 * [1557] Minimum Number of Vertices to Reach All Nodes
 */

// @lc code=start
class Solution
{
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>> &edges)
    {
        unordered_map<int, int> has;
        for (int i = 0; i < edges.size(); ++i)
        {
            has.insert({edges[i][1], 1});
        }
        vector<int> res;

        for (auto i = 0; i < n; ++i)
        {
            if(has.find(i) == has.end()) {
                res.push_back(i);
            }
        }

        return res;
    }
};
int main() {
    Solution s = Solution();
    vector<vector<int>> input = {{0,1},{0,2},{2,5},{3,4},{4,2}};
    
    s.findSmallestSetOfVertices(5, input);
    
    return 0;
}
// @lc code=end

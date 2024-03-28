/*
 * @lc app=leetcode id=1584 lang=cpp
 *
 * [1584] Min Cost to Connect All Points
 */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// @lc code=start

class Solution
{
public:
    int calculateDistance(const vector<int> &point1, const vector<int> &point2)
    {
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]);
    }

    int getMin(vector<vector<int>> graph, vector<int> &mst, int idx)
    {
        int min = INT_MAX;
        int index = -1;

        for (int i = 0; i < graph.size(); i++)
        {
            if (mst[idx])
                continue;
            if (!graph[i][idx])
                continue;
            int currunt_distance = calculateDistance(graph[i], graph[idx]);
            if (currunt_distance < min)
            {
                mst[i] = true;
                min = currunt_distance;
                index = i;
            };
        };
        if (index == -1) return true;
        return min;
    }
    // Function to calculate minimum cost to connect all points
    int minCostConnectPoints(vector<vector<int>> &points)
    {
        vector<int> mst(points.size(), false);
        
        for (int i = 0; i < points.size(); ++i) {
            // index.
            
        }

    }
};
// @lc code=end

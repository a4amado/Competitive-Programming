/*
 * @lc app=leetcode id=347 lang=cpp
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <unordered_map>

using namespace std;






struct ComparePairs
{
    bool operator()(const pair<int, int> &p1, const pair<int, int> &p2) const
    {
        return p1.second < p2.second;
    }
};

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        priority_queue<pair<int, int>, vector<pair<int, int>>, ComparePairs> pq;
        unordered_map<int, int> numMap;

        // Populate numMap
        for (auto &item : nums)
        {
            if (numMap.find(item) == numMap.end()) numMap[item] = 1;
            else numMap[item]++;
        }

        // Populate priority_queue with pairs
        for (auto it = numMap.begin(); it != numMap.end(); ++it)
        {
            pq.push(make_pair(it->first, it->second));
        }

        // Retrieve the top k frequent elements
        vector<int> result;
        for (int i = 0; i < k; i++)
        {
            result.push_back(pq.top().first);
            pq.pop();
        }

        return result;
    }
};





// @lc code=end

/*
 * @lc app=leetcode id=1046 lang=cpp
 *
 * [1046] Last Stone Weight
 */
#include <iostream>
#include <vector>
#include <queue>
#include <math.h>
using namespace std;

// @lc code=start

class Solution
{
public:
    int lastStoneWeight(vector<int> &stones)
    {
        priority_queue<int, vector<int>> mm;
        for (auto i : stones)
        {
            mm.push(i);
        }
        this->sol(mm);
        return mm.empty() ? 0 : mm.top();
    }

    void sol(priority_queue<int, vector<int>> &mm)
    {
        if (mm.size() < 2)
        {
            return;
        };

        int x = mm.top();
        mm.pop();
        int y = mm.top();
        mm.pop();
        int diff = std::abs(x - y);
        if (diff != 0)
        {
            mm.push(diff);
        }

        this->sol(mm);
    }
};

// @lc code=end

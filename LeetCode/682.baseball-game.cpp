/*
 * @lc app=leetcode id=682 lang=cpp
 *
 * [682] Baseball Game
 */
#include <iostream>
#include <vector>
#include <type_traits>

using namespace std;

// @lc code=start
class Solution
{
public:
    int calPoints(vector<string> &operations)
    {
        vector<int> l;

        for (auto a : operations)
        {
            // if int
            if (isdigit(a[a.size() - 1]))
            {
                l.push_back(stoi(a));
            }
            else if ("+" == a)
            {
                if (l.size() < 2)
                {
                    l.push_back(l.at(0));
                }
                else
                {
                    l.push_back(l.at(l.size() - 1) + l.at(l.size() - 2));
                }
            }
            else if (a == "C")
            {
                l.erase(l.end() - 1);
            }
            else if (a == "D")
            {
                if (!l.empty())
                {
                    l.push_back(l.back() * 2);
                }
            }
        }
        int sum = 0;
        for (auto i : l)
        {
            sum += i;
        };
        return sum;
    }
};
// @lc code=end

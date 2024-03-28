/*
 * @lc app=leetcode id=841 lang=cpp
 *
 * [841] Keys and Rooms
 */
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// @lc code=start
class Solution
{
public:
    bool canVisitAllRooms(vector<vector<int>> &rooms)
    {

        vector<bool> rooms_keys(rooms.size(), false);
        vector<bool> visited(rooms.size(), false);

        rooms_keys[0] = true;
        visited[0] = true;

        for (int i: rooms[0]) {
            rooms_keys[i] = true;
            dfs(rooms_keys, visited, i, rooms);
        }

        for (auto room : visited)
        {
            if (!room)
                return false;
        }

        return true;
    }

    void dfs(vector<bool> &rooms_keys, vector<bool> &visited, int room, vector<vector<int>> &rooms)
    {
        if (visited[room])
            return;
        if (!rooms_keys[room])
            return;

        visited[room] = true;
        for (auto key : rooms[room])
        {
            // add all keys to the arr
            rooms_keys[key] = true;
            visited[room] = true;
            dfs(rooms_keys, visited, key, rooms);
        }
    }
};

// @lc code=end
int main()
{
    Solution s = Solution();

    vector<vector<int>> d{{1 }, {2}, {3}, {}};
    bool ss = s.canVisitAllRooms(d);
    return 0;
}
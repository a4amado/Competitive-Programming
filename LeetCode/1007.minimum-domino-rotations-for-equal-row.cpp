#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <math.h>

using namespace std;

class Solution
{
public:
    int minDominoRotations(vector<int> &tops, vector<int> &bottoms)
    {
        unordered_map<int, int> m;
        int majority_number = 0;

        for (int idx = 0; idx < tops.size(); idx++)
        {
            int top_item = tops[idx];
            int bottom_item = bottoms[idx];

            if (tops[idx] == bottoms[idx])
            {
                bool exist = m.find(tops[idx]) != m.end();
                if (exist)
                    m[tops[idx]]++;
                else
                    m.emplace(tops[idx], 1);
                continue;
            }

            bool top_exist = m.find(tops[idx]) != m.end();
            if (top_exist)
                m[tops[idx]]++;
            else
                m.emplace(tops[idx], 1);

            bool bottom_exist = m.find(bottoms[idx]) != m.end();
            if (bottom_exist)
                m[bottoms[idx]]++;
            else
                m.emplace(bottoms[idx], 1);
        }

        auto most_frequent = max_element(m.begin(), m.end(), [](const auto &lhs, const auto &rhs)
                                         { return lhs.second < rhs.second; });

        if (most_frequent->second < tops.size())
            return -1;

        int number_of_times_the_most_frquent_number_appeared_in_the_top = 0;
        for (int item : tops)
        {
            if (item != most_frequent->first)
                continue;
            number_of_times_the_most_frquent_number_appeared_in_the_top++;
        };

                int number_of_times_the_most_frquent_number_appeared_in_the_bottom = 0;
        for (int item : bottoms)
        {
            if (item != most_frequent->first)
                continue;
            number_of_times_the_most_frquent_number_appeared_in_the_bottom++;
        };

        int max_freq = max(number_of_times_the_most_frquent_number_appeared_in_the_bottom, number_of_times_the_most_frquent_number_appeared_in_the_top);

        int mmmm = tops.size() - max_freq;

        return mmmm;
    }
};

int main()
{
    Solution s = Solution();
    vector<int> tops;

    tops.push_back(2);
    tops.push_back(1);
    tops.push_back(2);
    tops.push_back(4);
    tops.push_back(2);
    tops.push_back(2);

    vector<int> bottoms;
    bottoms.push_back(5);
    bottoms.push_back(2);
    bottoms.push_back(6);
    bottoms.push_back(2);
    bottoms.push_back(3);
    bottoms.push_back(2);

    cout << s.minDominoRotations(tops, bottoms) << endl;
    return 0;
}
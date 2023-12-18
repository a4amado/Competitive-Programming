#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const vector<int> q, const vector<int> b);

int main()
{

    int number_of_boxes_the_bag_can_hold, number_of_boxes = 0;

    cin >> number_of_boxes_the_bag_can_hold >> number_of_boxes;

    vector<vector<int>> n;

    for (int i = 0; i < number_of_boxes; i++)
    {
        vector<int> q;
        int g, b = 0;
        cin >> g >> b;

        q.push_back(g);
        q.push_back(b);

        n.push_back(q);
    }

    sort(n.begin(), n.end(), compare);

    int mm = 0;
    for (int i = 0; i < n.size(); i++)
    {

        if (number_of_boxes_the_bag_can_hold > 0)
        {
            if (number_of_boxes_the_bag_can_hold >= n.at(i).at(0))
            {
                mm = mm + (n.at(i).at(0) * n.at(i).at(1));
                number_of_boxes_the_bag_can_hold = number_of_boxes_the_bag_can_hold - n.at(i).at(0);
            } else {
                mm = mm + (number_of_boxes_the_bag_can_hold * n.at(i).at(1));
                number_of_boxes_the_bag_can_hold = 0;
            }



        }
    }

    cout << mm << endl;

    return 0;
}

bool compare(const vector<int> q, const vector<int> b)
{

    return q.at(1) > b.at(1);
}
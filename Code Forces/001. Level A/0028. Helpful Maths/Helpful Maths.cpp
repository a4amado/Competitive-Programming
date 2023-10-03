#include <iostream>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <utility>
#include <bits/stdc++.h>

using namespace std;

int main()
{

    char det[] = "+";
    string line;

    vector<int> nums;

    getline(cin, line);

    char *s = new char[line.length() + 1];

    strcpy(s, line.c_str());

    char *token;

    token = strtok(s, det);

    while (token != NULL)
    {
        int number = atoi(token);
        nums.push_back(number);
        token = strtok(NULL, det);
    }

    sort(nums.begin(), nums.end());

    for (int i = 0; i < (int)nums.size(); i++)
    {
        if (i != 0)
        {
            cout << '+';
        }
        cout << nums[i];
    }

    delete[] token;
    return 0;
}
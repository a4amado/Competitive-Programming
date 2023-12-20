/*
 * @lc app=leetcode id=605 lang=cpp
 *
 * [605] Can Place Flowers
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

// @lc code=start
class Solution
{
public:
   bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {


        int f = flowerbed.size();
        if (f == 1)
        {
            if (flowerbed[0] == 0)
            {
                if (n > 1)
                {
                    return false;
                }
                else
                {
                    return true;
                }
            } else {
                if (n == 0)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
        }

        for (int i = 0; i < flowerbed.size(); i++)
        {

            if (n == 0)
            {
                return true;
            }

            if (i == 0 && flowerbed[i] == 0)
            {
                if (flowerbed[1] == 0)
                {
                    flowerbed[i] = 1;
                    n--;
                }
            }

            else if (i == (flowerbed.size() - 1))
            {
                if (flowerbed[flowerbed.size() - 2] == 0 && flowerbed[flowerbed.size() - 1] == 0)
                {
                    flowerbed[i] = 1;
                    n--;
                }
            }
            else
            {
                if (flowerbed[i] == 0 && flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0)
                {
                    flowerbed[i] = 1;
                    n--;
                }
            }
        }
        return 0 >= n;
    }
};

// @lc code=end
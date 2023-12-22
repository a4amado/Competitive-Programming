/*
 * @lc app=leetcode id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */
#include <iostream>
#include <cstdint>

using namespace std;

// @lc code=start
class Solution
{
public:
    int64_t mySqrt(int64_t x)
    {

        if (x == 1 || x == 2) {
            return 1;
        }
        
        int64_t low = 0;
        int64_t high = x;
        int64_t mid = low + ((high + low) / 2);

        int64_t last_mid = 0;
        while (low <= high)
        {

            int64_t mid_square = mid * mid;
            if (mid_square == x)
            {
                return mid;
                break;
            }

            if (mid_square > x)
            {

                high = mid - 1;
            }

            if (mid_square < x)
            {
                last_mid = mid;
                low = mid + 1;
            }
            mid = (low + ((high - low) / 2));
        }
        return last_mid;
    }
};
// @lc code=kend

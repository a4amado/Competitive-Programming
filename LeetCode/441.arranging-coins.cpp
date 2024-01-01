/*
 * @lc app=leetcode id=441 lang=cpp
 *
 * [441] Arranging Coins
 */

// @lc code=start
class Solution
{
public:
int arrangeCoins(int n)
{
    float max = 1;
    float low = 1;
    float end = n;

    while (low <= end)
    {
        float mid = (end + low) / 2;
        float coins = (mid * (mid - 1)) / 2;

        if (coins * coins > n)
        {
            end = mid - 1;
        }
        else
        {
            max = mid;
            low = mid + 1;
        }
        
    }
    return max;
}};
// @lc code=end

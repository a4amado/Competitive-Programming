#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = 0
        high  = low + 1
        res = 0
        while high < len(prices):
            if prices[low] <= prices[high]:
                if prices[high] - prices[low] > res:
                    res = prices[high] - prices[low]
                high = high + 1
            else:
                low = low + 1
        return res

# s = Solution()
# s.maxProfit([7,1,5,3,6,4])
# @lc code=end


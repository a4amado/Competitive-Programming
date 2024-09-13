#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

from typing import List

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        count = 0
        coins.sort(reverse=True)
        
        for i in coins:
            if  amount == 0:
                break
            if amount >= i:
                c = amount // i
                amountDeducted = c * i
                count += c
                amount -= amountDeducted
        if amount == 0:
            return count
        else:
            return -1
                
        

# @lc code=end

s = Solution()

s.coinChange([186,419,83,408], 6249)


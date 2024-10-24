#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

from collections import Counter

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon = Counter("balloon")
        text = Counter(text)
        min_time = float('inf')
        for char in "balloon":
            min_time = min(min_time, text[char] // ballon[char])
        return min_time
    
# @lc code=end

text = "loonbalxballpoon"

sol = Solution()
print(
    sol.maxNumberOfBalloons(text)
)

#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

from typing import *

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustIn = {i: 0 for i in range(1, n+1)}
        trustedBy = {i: 0 for i in range(1, n+1)}

        for f, t in trust:
            trustIn[f] += 1
            trustedBy[f] += 1

        for i in range(1, n+1):
            if trust[i] == 0 and trustedBy[i] == n -1:return i
        return -1
# @lc code=end


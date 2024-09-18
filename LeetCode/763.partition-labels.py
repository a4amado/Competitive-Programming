#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
from typing import List

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # ababcbacadefegdehijhklij
        memo = {}
        for idx, char in enumerate(s):
            memo[char] = idx

        final = []
        sumOfFinal = 0
        maxTilNow = memo[s[0]]
        for idx, char in enumerate(s):
            # if curr idx is less than maxTilnow and the curr char reach
            # is more that the curr max
            # update the curr max
            maxTilNow = max(maxTilNow, memo[char])
            if idx == maxTilNow:
                lengthOfCurruntSegment = (idx + 1) - sumOfFinal
                final.append(lengthOfCurruntSegment)
                sumOfFinal = sumOfFinal + lengthOfCurruntSegment
            
        return final

# @lc code=end

s = Solution()
print(s.partitionLabels("eaaaabaaec"))
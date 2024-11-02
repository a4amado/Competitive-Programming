#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

from collections import Counter

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        count_ransom = Counter(ransomNote)

        for char, count in count_ransom.items():
            if count < count[char]:return False
        return True

        
# @lc code=end


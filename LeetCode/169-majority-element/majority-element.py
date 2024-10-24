from collections import Counter
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        l = list(count.items())
        l.sort(key=lambda x:x[1], reverse=True)
        return l[0][0]
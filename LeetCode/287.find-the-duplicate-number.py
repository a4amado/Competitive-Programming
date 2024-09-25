from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:
                return fast
    
# [1,3,4,2,2]

s = Solution()

print(s.findDuplicate([1,3,4,2,2]))

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        done = set()
        newArray = []
        for i in nums:
            if i not in done:
                newArray.append(i)
                done.add(i)
        
        for i in range(len(nums)):
            if i < len(newArray):
                nums[i] = newArray[i]
            else:
                nums[i] = '_'
        return len(newArray)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        unique = set(nums)
        
        for i in range(1, len(nums) + 1):
            if i not in unique:unique.add(i)
            else:unique.remove(i)
        return list(unique)

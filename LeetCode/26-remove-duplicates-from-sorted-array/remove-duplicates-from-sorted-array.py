class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        uniqie = set()
        for idx, item in enumerate(nums):
            uniqie.add(item)
        nums_ = [x for x in uniqie]
        for i in range(len(nums) - len(uniqie)):
            nums_.append("_")
        nums_.sort()
        for i in range(len(nums_)):
            nums[i] = nums_[i]
        return len(uniqie)

class Solution(object):
    def getConcatenation(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums)
        return nums
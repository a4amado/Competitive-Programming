class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
            
        # Iterate through each number in the array
        for num in nums:
            # Get the absolute value since the number might be negative due to previous marking
            index = abs(num) - 1
            
            # If the number at index is negative, we've seen this number before
            if nums[index] < 0:
                result.append(abs(num))
            # Otherwise, mark it as seen by making it negative
            else:
                nums[index] = -nums[index]
        
        return result
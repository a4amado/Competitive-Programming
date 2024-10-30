class NumArray:
    def __init__(self, nums: List[int]):
        # Create prefix sum array with one extra element at start
        self.prefix = [0] * (len(nums) + 1)
        
        # Calculate prefix sums
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
    
    def sumRange(self, left: int, right: int) -> int:
        # Return difference of prefix sums to get range sum
        return self.prefix[right + 1] - self.prefix[left]
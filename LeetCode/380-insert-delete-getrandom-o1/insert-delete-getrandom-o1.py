import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        - Using a list to store values for O(1) random access
        - Using a dict to store value -> index mapping for O(1) lookups
        """
        self.nums = []  # List to store actual values
        self.val_to_index = {}  # Dictionary to store value -> index mapping
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        Time complexity: O(1) average
        """
        if val in self.val_to_index:
            return False
            
        # Add value to end of list and update mapping
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        Time complexity: O(1) average
        """
        if val not in self.val_to_index:
            return False
            
        # Get the index of the value to remove
        index = self.val_to_index[val]
        last_val = self.nums[-1]
        
        # Move the last element to the position of the element to delete
        self.nums[index] = last_val
        self.val_to_index[last_val] = index
        
        # Remove the last element and update mapping
        self.nums.pop()
        del self.val_to_index[val]
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        Time complexity: O(1)
        """
        return random.choice(self.nums)
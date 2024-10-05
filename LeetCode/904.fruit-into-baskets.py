from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0  # left pointer for the sliding window
        maxRange = 0  # to keep track of the maximum number of fruits collected
        setOfFruits = {}  # a dictionary to track the last occurrence of each fruit type

        for i in range(len(fruits)):
            f = fruits[i]

            # Add the current fruit with its index to the dictionary
            setOfFruits[f] = i

            # If we have more than 2 types of fruits in the basket
            if len(setOfFruits) > 2:
                # Find the fruit type with the smallest last occurrence index
                min_index = min(setOfFruits.values())
                fruit_to_remove = [k for k, v in setOfFruits.items() if v == min_index][0]

                # Remove that fruit from the set
                del setOfFruits[fruit_to_remove]

                # Move the left pointer of the window to the right of the removed fruit's last occurrence
                l = min_index + 1

            # Calculate the maximum window size
            maxRange = max(maxRange, i - l + 1)

        return maxRange

        
# @lc code=end


s = Solution()
print(s.totalFruit([1,2,1]))
print(s.totalFruit([0,1,2,2]))
print(s.totalFruit([1,2,3,2,2]))
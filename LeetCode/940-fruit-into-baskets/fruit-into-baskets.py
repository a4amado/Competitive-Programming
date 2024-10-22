from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0  # left pointer for the sliding window
        r = 0
        maxRange = 0  # to keep track of the maximum number of fruits collected
        setOfFruits = {}  # a dictionary to track the last occurrence of each fruit type

        while r < len(fruits):
            setOfFruits[fruits[r]] = r
            r += 1

            if len(setOfFruits) > 2:
                
                # get idx of the of the smalleest fruiet
                items = list(setOfFruits.items())
                items.sort(key=lambda x:x[1])
                val, idx = items[0]
                del setOfFruits[val]
                l = idx + 1
            else:
                maxRange = max(maxRange, abs(l - r))
            

                
                


        

        return maxRange
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:return True
        if not flowerbed:
            return n == 0  # Return True if n is 0, as there are no plots to place flowers in
        
        i = 0
        while i < len(flowerbed):
            # Check if the current plot is empty and both adjacent plots (if they exist) are also empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                # Place a flower here
                flowerbed[i] = 1
                n -= 1
                # If we have placed enough flowers, we can return True early
                if n == 0:
                    return True
                # Skip the next plot to avoid placing adjacent flowers
                i += 2
            else:
                i += 1

        return n == 0

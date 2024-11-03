import bisect
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)
        res = []
        left = idx - 1
        right = idx
        
        while len(res) < k:
            span_to_left = abs(arr[left] - x) if left >= 0 else float('inf')
            span_to_right = abs(arr[right] - x) if right < len(arr) else float('inf')
            
            if span_to_left < span_to_right or (span_to_left == span_to_right and left >= 0):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1

        # Since we need to return the k closest elements in sorted order
        return sorted(res)[:k]
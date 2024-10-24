from typing import *
from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_list = deque(nums)
        i = 0
        while i < k:
            last_element = new_list.pop()
            new_list.appendleft(last_element)
            i += 1
        for idx, val in enumerate(new_list):
            nums[idx] = val

        
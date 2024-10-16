'''
    Time Complexity: O(N)
    Space Complexity: O(N)
    
    Where 'N' is the total number of elements in the array.
'''

import sys
sys.setrecursionlimit(10**7)
from typing import *

def twoSum(arr: List[int], target: int, n: int):
    table = {}

    for idx, val in enumerate(arr):
        remaining = target - table




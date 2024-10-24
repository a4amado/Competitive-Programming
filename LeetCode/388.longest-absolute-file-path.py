#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#
from typing import *

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        new_line = "\n"
        tab = "\t"
        def recursion(idx: int, level: int, map: Dict[str, D]):

            # find next \n
            i = idx
            while input[i:i+2] != new_line:i+=1

            pass
        recursion(0, 0)

# @lc code=end

s = """
dir
    tsubdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

"""

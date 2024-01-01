#
# @lc app=leetcode id=2011 lang=python
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        for idx in range(len(operations)):
            if operations[idx].startswith("-") or  operations[idx].endswith("-"):
                res = res - 1
            else:
                res = res  + 1
        return res
# @lc code=end


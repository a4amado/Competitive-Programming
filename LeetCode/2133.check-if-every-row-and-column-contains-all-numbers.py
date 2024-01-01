#
# @lc app=leetcode id=2133 lang=python
#
# [2133] Check if Every Row and Column Contains All Numbers
#

# @lc code=start


from operator import le


class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        for rows in range(0, len(matrix)):
            s = set()
            for columns in range(0, len(matrix)):
                if matrix[rows][columns] > len(matrix):
                    return False
                else:
                    s.add(matrix[rows][columns])
            if len(s) < len(matrix):
                return False
        for  columns in range(0, len(matrix)):
            s = set()
            for rows in range(0, len(matrix)):
                if matrix[rows][columns] > len(matrix):
                    return False
                else:
                    s.add(matrix[rows][columns])
            if len(s) < len(matrix):
                return False
        return True
# @lc code=end


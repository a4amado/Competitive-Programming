#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s: str):
        """
        :type s: str
        :rtype: bool
        """
        open = {
            "(": "(","[":"[", "{":"{"
        }
        close = {
            ")":")",
            "]":"]",
            "}": "}"
        }
        
        switch = {
            "(":")",
            ")":"(",
            "]":"[",
            "[":"]",
            "}": "{",
            "{": "}"
        }

        stack = []
        list_of = s.split()
        for idx, item in enumerate(s):
            if item in open:
                stack.append(item)
            if item in close:
                if len(stack) > 0 and  stack[-1] == switch[item]:
                    stack.pop()
                else:
                    stack.append(item)
        if len(stack) == 0:
            return True
        return False

ss = Solution()
print(ss.isValid("]"))

# @lc code=end


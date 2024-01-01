#
# @lc app=leetcode id=225 lang=python
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack(object):
    
    def __init__(self):
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)
        

    def pop(self):
        """
        :rtype: int
        """        
        return self.list.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.list[len(self.list) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.list) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end


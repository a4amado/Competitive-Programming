#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
from typing import Optional

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode]= None
# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:

        
        slow = head
        fast = head


        while  fast and fast.next:


            slow = slow.next
            fast = fast.next.next
            
            if slow.val == fast.val:
                return True
            
        return False


        # s = {}
        # curr = head
        # while curr != None:
        #     if s.get(str(hash(curr))) == 1:
        #         return True
        #     else:
        #         s[str(hash(curr))] = 1
        #     curr =curr.next
        # return False
# @lc code=end


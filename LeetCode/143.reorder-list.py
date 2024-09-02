#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
from math import ceil

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get the length of the list
        # slow-fast-pointer approace
        length = 0
        tracker = head
        while tracker:
            length+= length
            tracker = tracker.next

        slow = head
        fast = head
        
        # speedup the fas
        i = 1
        while i < ceil(length/2):
            fast = fast.next
            i += 1
 
        while fast:
            curr = fast
            fast = fast.next
            curr.next = slow.next
            slow.next = curr
            slow = slow.next
            

# @lc code=end


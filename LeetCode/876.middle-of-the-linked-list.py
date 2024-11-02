#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        currIdx = 0
        curr = head
        middle = 0
        middle = (length // 2) + 1
        
        while curr:
            if currIdx == middle:
                return curr
            curr = curr.next
            currIdx += 1
        
# @lc code=end


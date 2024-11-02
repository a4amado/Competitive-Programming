#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return float('-inf')
        
        after = self.removeNodes(head.next)

        if after.val > head.val:
            return after

        head.next = after
        return head
# @lc code=end


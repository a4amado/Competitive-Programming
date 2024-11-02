#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next or k == 0:
            return head
        
        # Calculate length of linked list
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
            
        # Adjust k if it's larger than length
        k = k % length
        if k == 0:
            return head
            
        # Connect tail to head to create cycle
        curr.next = head
        
        # Find the new breakpoint
        # To rotate right by k, we need to traverse (length - k) nodes
        steps_to_new_head = length - k
        curr = head
        for _ in range(steps_to_new_head - 1):
            curr = curr.next
            
        # Break the cycle and return new head
        new_head = curr.next
        curr.next = None
        
        return new_head
# @lc code=end


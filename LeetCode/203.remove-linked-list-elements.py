#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
from tkinter import NO
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        next = curr.next
        prev_node = None

        while curr:
            if curr.val == val:
                if not prev_node:
                    if curr.next:
                        head = head.next
                        curr = head
                        next = curr.next
                    else:
                        head = None
                        curr = None
                elif not curr.next:
                    prev_node.next = None
                    curr = None
                else:
                    prev_node.next = next
                    curr = next
                    next = next.next

            else:
                if curr.next:
                    prev_node = curr
                    curr = next
                    next = next.next
                else:
                    curr = None
        return head

# @lc code=end

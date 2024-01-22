#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get len
        # go to the mid
        # compare from mid and the begging
        curr = head
        l = 0
        while curr:
            l+=1
            curr = curr.next

        mid = math.ceil(l / 2)
        another_head = None
        # reverse first half
        i = 0
            
        while i < mid:
            if not another_head:
                another_head = ListNode(head.val)
                head = head.next
                i+=1
                continue
            node = ListNode(head.val)
            node.next = another_head
            another_head = node
            head = head.next
            i+=1
        if l % 2 != 0:
            another_head = another_head.next
        while another_head and head:
            if another_head.val != head.val:
                return False
            another_head = another_head.next
            head = head.next
        return True
# @lc code=end


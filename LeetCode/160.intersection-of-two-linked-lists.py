#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
from typing import List

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        uniqie = set()
        curr = headA
        while curr:
            uniqie.add(curr.val)
            curr = curr.next

        curr = headB
        ans = None
        while curr:
            if curr.val in uniqie:
                ans = curr
            curr = curr.next
        return ans
# @lc code=end


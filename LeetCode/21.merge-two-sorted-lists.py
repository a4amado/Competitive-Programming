#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val = 0, next=None):
        self.val= val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list_new = ListNode()
        last_element = list_new

        while list1 and list2:
            if (list1.val < list2.val):
                # append the new element to the last node
                last_element.next = ListNode(list1.val)
                # update the last element
                last_element = last_element.next
                # remove element from the list
                list1 = list1.next
            else:
                # append the new element to the last node
                last_element.next = ListNode(list2.val)
                # update the last element
                last_element = last_element.next
                # remove element from the list
                list2 = list2.next
        if list1:
            last_element.next = list1
        if list2:
            last_element.next = list2
        list_new = list_new.next
        return list_new
# @lc code=end


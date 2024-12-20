# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        after = self.removeNodes(head.next)

        if after.val > head.val:
            return after

        head.next = after
        return head
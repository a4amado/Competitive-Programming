class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if  not head or not head.next:
            return head

        next = self.deleteDuplicates(head.next)

        if next.val == head.val:
            return next

        head.next = next

        return head
class Solution:
    def merge(self, head: Optional[ListNode], other_head: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy node to handle edge cases
        dummy = ListNode(0)
        curr = dummy
        
        # Compare and merge while both lists have nodes
        while head and other_head:
            if head.val <= other_head.val:
                curr.next = head
                head = head.next
            else:
                curr.next = other_head
                other_head = other_head.next
            curr = curr.next
            
        # Attach remaining nodes if any
        if head:
            curr.next = head
        if other_head:
            curr.next = other_head
            
        return dummy.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases
        if not head or not head.next:
            return head
            
        # Find middle of the list using slow and fast pointers
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Split the list into two halves
        second_half = slow.next
        slow.next = None  # Break the link
        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(second_half)
        
        # Merge the sorted halves
        return self.merge(left, right)
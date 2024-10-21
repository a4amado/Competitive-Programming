from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # Base case: if there are fewer than 2 nodes, no swap
            return head

        # Pointers to the first and second node to be swapped
        first = head
        second = head.next

        # Swap the first and second nodes
        first.next = self.swapPairs(second.next)  # Recursively swap the rest of the list
        second.next = first  # Point the second node to the first

        # The new head is the second node after the swap
        return second
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        unique_nodes = set()
        
        # Traverse the first linked list and add each node to the set
        curr = headA
        while curr:
            unique_nodes.add(curr)  # Store the node itself, not its value
            curr = curr.next

        # Traverse the second linked list and check if any node is in the set
        curr = headB
        while curr:
            if curr in unique_nodes:
                return curr  # Intersection found
            curr = curr.next

        return None  # No intersection found

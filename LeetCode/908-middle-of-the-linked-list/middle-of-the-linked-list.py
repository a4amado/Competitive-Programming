class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        currIdx = 0
        curr = head
        middle = 0
        middle = (length // 2) + 1
        
        while curr:
            if currIdx == middle - 1:
                return curr
            curr = curr.next
            currIdx += 1
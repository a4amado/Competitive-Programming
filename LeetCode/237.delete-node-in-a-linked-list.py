class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        
        node.val, node.next.val = node.next.val, node.val
        if node and node.next and not node.next.next: 
            node.next = None
            return
        self.deleteNode(node.next)
        
        
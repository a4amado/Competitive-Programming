from typing import Optional, Dict

class DoublyLinkedListNode:
    def __init__(self, val: int) -> None:
        self.prev: Optional[DoublyLinkedListNode] = None
        self.next: Optional[DoublyLinkedListNode] = None
        self.val = val
        self.key: Optional[int] = None  # Track the key for deletion in hashmap

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[DoublyLinkedListNode] = None
        self.tail: Optional[DoublyLinkedListNode] = None
        self.len = 0

    def remove(self, node: DoublyLinkedListNode):
        """Remove a node from the list."""
        if not node.prev:
            # Node is the head
            self.head = node.next
        else:
            node.prev.next = node.next

        if not node.next:
            # Node is the tail
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        node.prev = None
        node.next = None
        self.len -= 1

    def append(self, node: DoublyLinkedListNode):
        """Add a node to the end of the list (most recent)."""
        if not self.tail:
            # Empty list
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.len += 1

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap: Dict[int, DoublyLinkedListNode] = {}
        self.list = DoublyLinkedList()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1  # Key not found
        
        # Retrieve node
        node = self.hashMap[key]
        
        # Move the node to the end (most recently used)
        self.list.remove(node)
        self.list.append(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            # Update the value and move to the end
            node = self.hashMap[key]
            node.val = value
            self.list.remove(node)
            self.list.append(node)
        else:
            # Create a new node
            newNode = DoublyLinkedListNode(value)
            newNode.key = key

            if self.list.len == self.cap:
                # Cache is full, evict the least recently used (head)
                lru_node = self.list.head
                if lru_node:
                    del self.hashMap[lru_node.key]
                    self.list.remove(lru_node)

            # Add new node to the cache and list
            self.list.append(newNode)
            self.hashMap[key] = newNode

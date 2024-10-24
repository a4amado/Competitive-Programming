
from collections import deque

class MyHashSet:
    def __init__(self):
        self.map = [deque([]) for _ in range(1000)]
        
    def add(self, key: int, value: int) -> None:
        hash_key = key % 1000
        idx = self.get_idx(key)
        
        if idx == -1:
            # Key doesn't exist, simply append
            self.map[hash_key].append([key, value])
        else:
            # Key exists, rotate, remove old value, rotate back
            self.map[hash_key].rotate(-idx)
            self.map[hash_key].popleft()  # Remove from front after rotation
            self.map[hash_key].rotate(idx)  # Rotate back to original position
            self.map[hash_key].append([key, value])
            
    def get(self, key: int) -> int:
        hash_key = key % 1000
        for old_key, val in self.map[hash_key]:
            if old_key == key:
                return val
        return -1
    
    def get_idx(self, key: int) -> int:
        hash_key = key % 1000
        for idx, (old_key, val) in enumerate(self.map[hash_key]):
            if old_key == key:
                return idx
        return -1
    
    def remove(self, key: int) -> None:
        hash_key = key % 1000
        idx = self.get_idx(key)
        
        if idx == -1:
            return
            
        self.map[hash_key].rotate(-idx)
        self.map[hash_key].popleft()  # Remove from front after rotation
        self.map[hash_key].rotate(idx)  # Rotate back to original position
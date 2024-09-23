#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream

from typing import List
#
import heapq

# @lc code=start
class KthLargest:
    data: List[int] = []
    kth = None
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k and nums:
            heapq.heappop(nums)
        self.data = nums
        
        self.kth = k

    def add(self, val: int) -> int:
        if not self.data:
            self.data.append(val)
            return self.data[0]
        
        if len(self.data) < self.kth:
            heapq.heappush(self.data, val)
            return self.data[0]


        if val <= self.data[0]:
            return self.data[0]
        
        self.data[0] = val
        # heapify
        currIdx = 0

        while True:
            
            idx = None

            # left child
            leftChildIdx = (currIdx * 2) + 1
            # right child
            rightChildIdx = (currIdx * 2) + 2

            if leftChildIdx >= len(self.data) and rightChildIdx >= len(self.data):
                break


            if leftChildIdx >= len(self.data) and not (rightChildIdx >= len(self.data)):
                idx = rightChildIdx
            elif not (leftChildIdx >= len(self.data)) and rightChildIdx >= len(self.data):
                idx = leftChildIdx


            idx = idx if idx != None else leftChildIdx if self.data[leftChildIdx] <= self.data[rightChildIdx] else rightChildIdx

            if self.data[idx] < self.data[currIdx]:
                self.data[idx], self.data[currIdx] = self.data[currIdx], self.data[idx]
                currIdx = idx
            else:
                break


            
            
        
        
        return self.data[0]
        
        
# kthLargest = KthLargest(3, [4, 5, 8, 2])
# print(kthLargest.add(3))
# print(kthLargest.add(5))
# print(kthLargest.add(10))
# print(kthLargest.add(9))
# print(kthLargest.add(4))
#  [[4, []], [2], [10], [9], [9]]

# kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
# print(kthLargest.add(1))
# print(kthLargest.add(10))
# print(kthLargest.add(9))
# print(kthLargest.add(9))
[[1,[]],[-3],[-2],[-4],[0],[4]]
kthLargest = KthLargest(1, [])
print(kthLargest.add(-3))
print(kthLargest.add(-2))
print(kthLargest.add(-4))
print(kthLargest.add(0))
print(kthLargest.add(4))

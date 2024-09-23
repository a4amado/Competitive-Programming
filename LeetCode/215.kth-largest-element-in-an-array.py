#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

from typing import List
import heapq

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        n = len(nums)
        idx = 0
        i = 0
        while idx < len(nums):
            if len(minHeap) < k:
                heapq.heappush(minHeap, nums[idx])
                idx += 1
            else:
                # replace
                if nums[idx] <= minHeap[0]:
                    idx+=1
                    continue
                else:
                    minHeap[0] = nums[idx]
                    # then heapify down
                    i = 0
                    while i < len(minHeap):
                        leftChildIdx = (i * 2) + 1
                        leftChildIdxOutOfBound = leftChildIdx >= len(minHeap)
                        rightChildIdx = (i * 2) + 2
                        rightChildIdxOutOfBound = rightChildIdx >= len(minHeap)
                        
                        idxToUse = None

                        if leftChildIdxOutOfBound and rightChildIdxOutOfBound:
                            idx += 1
                            break
                        if leftChildIdxOutOfBound and not rightChildIdxOutOfBound:
                            idxToUse = rightChildIdx
                        elif not leftChildIdxOutOfBound and rightChildIdxOutOfBound:
                            idxToUse = leftChildIdx
                
                        idxToUse = idxToUse if idxToUse != None else leftChildIdx if minHeap[leftChildIdx] <= minHeap[rightChildIdx] else rightChildIdx

                        if minHeap[idxToUse] < minHeap[i]:
                            minHeap[idxToUse],  minHeap[i] = minHeap[i], minHeap[idxToUse]
                            i = idxToUse
                        else:
                            idx += 1
                            break
                        
        return minHeap[0]


                

# @lc code=end


s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],  4))
from collections import deque
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        # BFS setup: queue stores (index, number of jumps to reach this index)
        queue = deque([(0, 0)])  # Start from index 0 with 0 jumps
        visited = set()  # To track visited positions
        visited.add(0)
        
        while queue:
            idx, jumps = queue.popleft()
            
   
            # Explore all possible jumps from curr jump
            for i in range(idx + 1, min(idx + nums[idx] + 1, len(nums))):

                if len(nums) - 1 == i:
                    return jumps + 1
                if i not in visited:
                    queue.append((i, jumps + 1))
                visited.add(i)

        return -1  # In case no solution is found, though problem guarantees a solution


# @lc code=end

s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([3,4,3,2,5,4,3]))
print(s.jump([4,1,1,3,1,1,1]))
print(s.jump([10,9,8,7,6,5,4,3,2,1,1,0]))




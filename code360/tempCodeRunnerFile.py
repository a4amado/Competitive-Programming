
# def frogJump(n: int, heights: List[int], steps: int) -> int:
    
#     dp = [0] * len(heights)
    
#     for i in range(len(heights)):
#         begin = max(abs(steps - i), 0)
#         end = min(len(heights), begin + steps + 1)
#         for j in range(begin, end):
#             dp[i] = min(dp[i], dp[j] + abs(heights[i] - heights[j]))
    
#     return dp[-1]

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Create a suffix sum array to store the remaining stones from each pile to the end
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]
        
        # Memoization table: dp[i][M] represents the max stones Alice can get starting from pile i with current M
        dp = [[0] * (n + 1) for _ in range(n)]
        
        # Recursive function to find the maximum stones Alice can collect
        def maxStones(i, M):
            # If we are at the last piles, Alice can take all remaining stones
            if i >= n:
                return 0
            # If the remaining piles can be taken in one move, take them all
            if 2 * M >= n - i:
                return suffix_sum[i]
            # If the result is already computed, return it
            if dp[i][M] > 0:
                return dp[i][M]
            
            # Minimax: Alice wants to maximize her stones, Bob minimizes them
            max_stones = 0
            for X in range(1, 2 * M + 1):
                # Bob will try to minimize the remaining stones Alice can get
                max_stones = max(max_stones, suffix_sum[i] - maxStones(i + X, max(M, X)))
            
            # Store the result in dp table
            dp[i][M] = max_stones
            return max_stones
        
        return maxStones(0, 1)

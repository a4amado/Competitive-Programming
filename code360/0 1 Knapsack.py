def solve_knapsack(n, weights, values, maxWeight):
    # visited = {}
    # def b(idx: int, weightRemaining: int):
    #     if idx == len(weights):
    #         return 0
    #     if (idx, weightRemaining) in visited:
    #         return visited[(idx, weightRemaining)]
    #     v = b(idx+1, weightRemaining)  # Don't take the item
    #     if weights[idx] <= weightRemaining:
    #         v = max(v, values[idx] + b(idx+1, weightRemaining - weights[idx]))  # Take the item
    #     visited[(idx, weightRemaining)] = v
    #     return v
    # return b(0, maxWeight)
    dp = [[0 for i in range(maxWeight + 1)] for i in range(len(weights) + 1)]

    for idx in range(1, len(dp)):
        for j in range(len(dp[0])):
            dp[idx][j] = dp[idx-1][j]
            
            if weights[idx -1] <= j:
                dp[idx][j] = max(dp[idx -1][j], values[idx - 1] + dp[idx - 1 ][j - weights[idx - 1]])  # Take the item
    return dp[-1][maxWeight]
    # def solve_knapsack(n, weights, values, maxWeight):
    #     dp = [[0 for j in range(maxWeight + 1)] for i in range(n + 1)]
        
    #     for i in range(1, n + 1):
    #         for w in range(maxWeight + 1):
    #             if weights[i-1] <= w:
    #                 dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
    #             else:
    #                 dp[i][w] = dp[i-1][w]
        
    #     return dp[n][maxWeight]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        weights = list(map(int, input().split()))
        values = list(map(int, input().split()))
        W = int(input())
        result = solve_knapsack(N, weights, values, W)
        print(result)

if __name__ == "__main__":
    main()
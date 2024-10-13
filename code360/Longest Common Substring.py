def lcs(str1: str, str2: str) -> str:
    dp = [[0 for i in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    max_val, max_y, max_x = 0, 0, 0
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_val:
                    max_val = dp[i][j]
                    max_y, max_x = i, j
    return str1[max_x-max_val:max_x]

str1 = "abcjklp"
str2 = "acjkp"

result = lcs(str1, str2)
print(f"Longest Common Subsequence: {result}")
print(f"Length of LCS: {len(result)}")
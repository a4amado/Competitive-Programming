
def shortestSupersequence(str1: str, str2: str) -> str:
    dp = [[0 for i in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j  - 1])
    
    # contruct
    y, x, = len(dp) -1, len(dp[0]) -1
    s = []
    while y > 0 and x > 0:
        if str1[x - 1] == str2[y - 1]:
            s.append(str1[x - 1])
            y -= 1
            x -= 1
        elif dp[y - 1][x] > dp[y][x - 1]:
            s.append(str2[y - 1])
            y -= 1
        else:
            s.append(str1[x - 1])
            x -= 1

    while y > 0:
        s.append(str2[y-1])
        y-=1

    while x > 0:
        s.append(str1[x-1])
        x -= 1
        
    return "".join(reversed(s))


A = "brute" 
B = "groot"


print(
    shortestSupersequence(A, B)
)

A = "brute"
B = "groot"
print(shortestSupersequence(A, B))


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0 for i in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if str1[j - 1] == str2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j  - 1])
        
        # contruct
        y, x, = len(dp) -1, len(dp[0]) -1
        s = []
        while y > 0 and x > 0:
            if str1[x - 1] == str2[y - 1]:
                s.append(str1[x - 1])
                y -= 1
                x -= 1
            elif dp[y - 1][x] > dp[y][x - 1]:
                s.append(str2[y - 1])
                y -= 1
            else:
                s.append(str1[x - 1])
                x -= 1

        while y > 0:
            s.append(str2[y-1])
            y-=1

        while x > 0:
            s.append(str1[x-1])
            x -= 1
            
        return "".join(reversed(s))

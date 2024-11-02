'''
Input: X = 'ABCBDAB', Y = 'BDCABA'
Output: 9
Explanation: The SCS are 'ABCBDCABA', 'ABDCABDAB', and 'ABDCBDABA', having length 9.

'''

class Solution:
	def findSCSLength(self, X: str, Y: str) -> int:
		dp = [[0 for _ in range(len(X) + 1)] for _ in range(len(Y) + 1)]
		
		for i in range(1,len(dp)):
			for j in range(1,len(dp[0])):
				if  X[j-1] == Y[i -1]:
					dp[i][j] = dp[i-1][j-1] + 1
				else:
					dp[i][j] = max(dp[i-1][j], dp[i][j-1])
		print(dp)
X = 'ABCBDAB'
Y = 'BDCABA'
sol = Solution()

sol.findSCSLength(X, Y)

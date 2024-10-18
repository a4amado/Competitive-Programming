class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustIn = {i: 0 for i in range(1, n+1)}
        trustedBy = {i: 0 for i in range(1, n+1)}

        for f, t in trust:
            trustIn[f] += 1
            trustedBy[t] += 1

        for i in range(1, n+1):
            if trustIn[i] == 0 and trustedBy[i] == n -1:return i
        return -1

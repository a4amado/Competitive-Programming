
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
            
        wildcard = "*"
        singular = "?"
        memo = {}
        def d(idx:int, jdx: int):
            if idx == len(pattern) and jdx == len(text):
                return True
            if idx == len(pattern):
                return False
            if jdx == len(text):
                return all(char == wildcard for char in pattern[idx:])

            key = (idx, jdx)
            if key in memo: return memo[key]
            

            currChar = text[jdx]
            currpattern = pattern[idx]

            if currpattern == singular:
                memo[key] = d(idx+1, jdx+1)
            elif wildcard == currpattern:
                memo[key] = d(idx+1, jdx) or d(idx, jdx+1)
            elif currpattern != currChar:
                memo[key] = False
            else:
                memo[key] = d(idx + 1, jdx + 1)
            
            
            return memo[key]
        return d(0,0)
            


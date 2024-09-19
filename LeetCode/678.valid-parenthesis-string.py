class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        
        def backtracking(idx: int, oq: List[str], cq: List[str]):
            if (idx, tuple(oq), tuple(cq)) in memo:
                return memo[(idx, tuple(oq), tuple(cq))]
            
            if idx == len(s):
                return len(oq) == 0 and len(cq) == 0
            
            res = False
            
            if s[idx] == "(":
                oq.append("(")
                cq.append("(")
                res = backtracking(idx + 1, oq, cq)
                if res:
                    memo[(idx, tuple(oq), tuple(cq))] = True
                    return True
                oq.pop()
                cq.pop()
            elif s[idx] == ")":
                if oq and oq[-1] == "(" and cq  and cq[-1] == "(":
                    oq_temp, cq_temp = oq.pop(), cq.pop()
                    res = backtracking(idx + 1, oq, cq)
                    if res:
                        memo[(idx, tuple(oq), tuple(cq))] = True
                        return True
                    oq.append(oq_temp)
                    cq.append(cq_temp)
            else:  # s[idx] == '*'
                # Try '*' as empty
                res = backtracking(idx + 1, oq, cq)
                if res:
                    memo[(idx, tuple(oq), tuple(cq))] = True
                    return True
            
                # Try '*' as '('
                oq.append("(")
                cq.append("(")
                res = backtracking(idx + 1, oq, cq)
                if res:
                    memo[(idx, tuple(oq), tuple(cq))] = True
                    return True
                oq.pop()
                cq.pop()
            
                if not res and oq and cq and oq[-1] == "(" and cq[-1] == "(":
                    # Try '*' as ')'
                    oq_temp, cq_temp = oq.pop(), cq.pop()
                    res = backtracking(idx + 1, oq, cq)
                    if res:
                        memo[(idx, tuple(oq), tuple(cq))] = True
                        return True
                    oq.append(oq_temp)
                    cq.append(cq_temp)
            
            memo[(idx, tuple(oq), tuple(cq))] = False
            return res
        
        return backtracking(0, [], [])
    

class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        string containing ( ) *

        valid string 
            - ( has a )
            - ) has a (
            - ( must be before )
            - * can be ( or ) or ""

        keep track of a count:
            if ( -> + 1
            if ) -> -1 
            if * -> +1/-1

        """
        # Time Complexity - O(N)
        # Space Complexity - O(1)
        leftMin, leftMax = 0, 0

        for c in s:
            if c =="(":
                leftMin += 1
                leftMax += 1

            elif c == ")":
                leftMin -= 1
                leftMax -= 1

            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
            
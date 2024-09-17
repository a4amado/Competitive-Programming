def lcs(a, b):
    visited = {}
    def dp(strA: str, strB: str):
        if not strA or not strB:
            return 0

        uniqueKey = hash(f'{strA},{strB}')
        if uniqueKey in visited:
            return visited[uniqueKey]
        
        

        if strA[0] == strB[0]:
            visited[uniqueKey] = 1 + dp(strA[1:], strB[1:])
            return visited[uniqueKey]
        
        visited[uniqueKey] = max(dp(strA[1:], strB), dp(strA, strB[1:]))
        return visited[uniqueKey]
    return dp(text1, text2)

print(lcs("abcde", "ace"))


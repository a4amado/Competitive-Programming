from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        parent = {}
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(account[1], email)
        
        merged = defaultdict(list)
        for email in parent:
            merged[find(email)].append(email)
        
        return [[email_to_name[emails[0]]] + sorted(emails) for emails in merged.values()]
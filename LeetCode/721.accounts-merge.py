#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
from typing import *
from collections import defaultdict
# @lc code=start

from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # set every email to it's own parent
        for account in accounts:
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email


        
        for account in accounts:
            # only assosiate the first email with a name
            name = account[0]
            email_to_name[account[1]] = name
            firstEmailOfTheList = account[1]

            # assosiant every email with the first email of the list
            for email in account[2:]:
                union(firstEmailOfTheList, email)

        

        merged = defaultdict(list)
        
        for email in parent:
            merged[find(email)].append(email)
        
        return [[email_to_name[emails[0]]] + sorted(emails) for emails in merged.values()]
        




            
            
# @lc code=end

s = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(s.accountsMerge(accounts))
accounts = [["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]]

print(s.accountsMerge(accounts))
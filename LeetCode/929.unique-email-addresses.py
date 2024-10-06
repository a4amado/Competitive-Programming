#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#
from typing import *

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = set()
        for email in emails:
            e = []
            [localName, domainName] = email.split("@")
            localName = "".join(localName.split("+")[0].split("."))
            e.append(localName)
            e.append("@")
            e.append(domainName)
            d.add("".join(e))
        return len(d)
        

# @lc code=end

s = Solution()
print(s.numUniqueEmails(
    [
    "test.email+alex@leetcode.com",
     "test.e.mail+bob.cathy@leetcode.com",
     "testemail+david@lee.tcode.com"
     ]

))
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                # Person i buys min(tickets[i], tickets[k]) tickets
                time += min(tickets[i], tickets[k])
            else:
                # People after k buy at most tickets[k] tickets
                time += min(tickets[i], tickets[k] - 1)
        return time

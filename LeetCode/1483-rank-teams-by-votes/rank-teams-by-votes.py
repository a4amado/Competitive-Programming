from typing import *
from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # Create a dictionary to store vote counts for each position for each team
        ranks = {char: {
            idx + 1: 0 for idx in range(len(votes[0]))
        } for char in votes[0]}

        # Count votes for each position
        for idx in range(len(votes[0])):
            for jdx in range(len(votes)):
                char = votes[jdx][idx]
                ranks[char][idx + 1] += 1
        
        # Convert to list for sorting
        teams = list(ranks.keys())
        
        # Custom sort function that compares teams based on votes at each position
        def compare_teams(a, b):
            for pos in range(1, len(votes[0]) + 1):
                if ranks[a][pos] != ranks[b][pos]:
                    return ranks[b][pos] - ranks[a][pos]
            return ord(a) - ord(b)  # If all positions tie, sort alphabetically
        
        # Sort teams using the custom comparison
        sorted_teams = sorted(teams, key=functools.cmp_to_key(compare_teams))
        
        # Join the sorted teams into final string
        return ''.join(sorted_teams)
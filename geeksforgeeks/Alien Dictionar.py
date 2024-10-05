#User function Template for python3

from typing import *
         

from typing import List, Dict

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        keyIdx = {}
        chatIdx = {}
        uniqueChars = []
        
        # Collect all unique characters
        for word in dict:
            for char in word:
                if char not in uniqueChars:
                    uniqueChars.append(char)
        
        for idx, char in enumerate(uniqueChars):
            keyIdx[char] = idx
            chatIdx[idx] = char

        adjs = [[] for _ in range(len(uniqueChars))]

        # Create adjacency list based on character precedence
        for wordIdx in range(len(dict) - 1):
            word = dict[wordIdx]
            nextWord = dict[wordIdx + 1]
            for idx in range(min(len(word), len(nextWord))):
                currChar = word[idx]
                nextChar = nextWord[idx]
                if currChar != nextChar:
                    adjs[keyIdx[currChar]].append(keyIdx[nextChar])
                    break  # Only consider the first differing character

        # Cycle detection using DFS
        def detect_cycle(idx: int, selfVisited: List[int], visited: List[int]) -> bool:
            if idx in selfVisited:  # Back edge found, indicating a cycle
                return True
            selfVisited.append(idx)
            visited.append(idx)  # Mark as fully processed
            for neighbor in adjs[idx]:
                if neighbor not in visited and detect_cycle(neighbor, selfVisited, visited):
                    return True

            selfVisited.pop()
            
            return False
        
        # Check for cycles in the graph
        visited = []
        for i in range(len(adjs)):
            if i not in visited:
                if detect_cycle(i, [], visited):
                    return ""  # Return empty string if cycle is detected

        # Topological sort using DFS
        visited_set = set()
        result = []

        def topological_dfs(idx: int):
            if idx in visited_set:
                return
            visited_set.add(idx)
            for neighbor in adjs[idx]:
                topological_dfs(neighbor)
            result.append(chatIdx[idx])

        # Call DFS for all nodes
        for i in range(len(uniqueChars)):
            if i not in visited_set:
                topological_dfs(i)
        
        return "".join(result[::-1])  # Reverse result to get correct order


s = Solution()
print(
    s.findOrder( ["baa", "abcd", "abca", "cab", "cad"],0,0)
)
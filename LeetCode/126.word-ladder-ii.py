from collections import deque
from typing import List, DefaultDict
from collections import defaultdict

class Solution:
    def is_one_char_difference(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        diff_count = 0
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count == 1

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList.insert(0, beginWord)
        wordList.append(endWord)
        
        # Create adjacency list for all words that are one char apart
        adjs = [set() for _ in range(len(wordList))]
        patterns = defaultdict(list)
        for idx, word in enumerate(wordList):
            for i in range(len(word)):
                patt = word[:i] + "*" + word[i+1:]
                patterns[patt].append(idx)
        for l in patterns.values():
            if len(l) < 2:
                continue
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    adjs[l[i]].add(l[j])
                    adjs[l[j]].add(l[i])

        queue = deque([[0]])
        visited = set()
        result = []
        min_level = float('inf')

        while queue:
            path = queue.popleft()
            current = path[-1]

            if len(path) > min_level:
                break

            if current == len(wordList) - 1:
                result.append([wordList[i] for i in path])
                min_level = len(path)
                continue

            for nei in adjs[current]:
                if nei in visited:
                    continue
                new_path = path + [nei]
                queue.append(new_path)

            visited.add(current)

        return result

# Test the solution
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
s = Solution()
print(s.findLadders(beginWord, endWord, wordList))
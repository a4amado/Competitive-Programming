from typing import List
from collections import deque

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Create a dictionary of operations, sorted by index
        operations = sorted(zip(indices, sources, targets), key=lambda x: -x[0])
        ss = {}
        for idx, src, target in operations:
            if idx not in ss:
                ss[idx] = []
            ss[idx].append({'src': src, 'target': target})

        final = deque([])
        i = 0
        while i < len(s):
            if i not in ss:
                final.appendleft(s[i])
                i += 1
            else:
                max_length = 0
                replacement = None
                for op in ss[i]:
                    src = op['src']
                    target = op['target']
                    if s[i:i+len(src)] == src and len(src) > max_length:
                        max_length = len(src)
                        replacement = target
                
                if replacement:
                    final.appendleft(replacement)
                    i += max_length
                else:
                    final.appendleft(s[i])
                    i += 1

        final.reverse()
        return "".join(final)
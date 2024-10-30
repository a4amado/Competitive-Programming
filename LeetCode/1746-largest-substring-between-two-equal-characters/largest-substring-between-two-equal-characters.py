class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idxs = defaultdict(list)
        for idx, char in enumerate(s):
            idxs[char].append(idx)
        max_range = float('-inf')

        for row in idxs.values():
            minVal = min(row)
            maxVal = max(row)
            max_range = max(max_range, abs(minVal - maxVal) -1)

        return -1 if max_range == float('-inf') else max_range
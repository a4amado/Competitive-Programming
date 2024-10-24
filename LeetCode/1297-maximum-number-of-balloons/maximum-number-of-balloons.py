class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon = Counter("balloon")
        text = Counter(text)
        min_time = float('inf')
        for char in "balloon":
            min_time = min(min_time, text[char] // ballon[char])
        return min_time
    
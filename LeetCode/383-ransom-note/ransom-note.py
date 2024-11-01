class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        count_ransom = Counter(ransomNote)

        for char, counts in count_ransom.items():
            if counts > count[char]:return False
        return True
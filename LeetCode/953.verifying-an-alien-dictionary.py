
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a dictionary that maps each character to its index in the alien language
        order_map = {char: idx for idx, char in enumerate(order)}
        
        # Comparator function for `cmp_to_key`
        def compare_teams(word1, word2):
            for char1, char2 in zip(word1, word2):
                if order_map[char1] != order_map[char2]:
                    return order_map[char1] - order_map[char2]
            # If all characters are the same in the shorter word, compare by length
            return len(word1) - len(word2)
        
        # Sort the words using the alien order comparator
        sorted_words = sorted(words, key=functools.cmp_to_key(compare_teams))

        # Check if the sorted list matches the original list
        return words == sorted_words
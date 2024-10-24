#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, binary_string: str) -> int:
        # Convert string characters to integers
        binary_digits = [int(digit) for digit in binary_string]
        
        # First approach: keep first digit unchanged and make rest alternating
        changes_keeping_first = 0
        for i in range(1, len(binary_string)):
            if binary_digits[i] == binary_digits[i-1]:  # If current equals previous
                binary_digits[i] = 1 - binary_digits[i]  # Flip current digit
                changes_keeping_first += 1
        
        # Second approach: flip first digit and make rest alternating
        binary_digits = [int(digit) for digit in binary_string]  # Reset array
        binary_digits[0] = 1 - binary_digits[0]  # Flip first digit
        changes_with_first_flipped = 1  # Start with 1 because we flipped first digit
        
        for i in range(1, len(binary_string)):
            if binary_digits[i] == binary_digits[i-1]:  # If current equals previous
                binary_digits[i] = 1 - binary_digits[i]  # Flip current digit
                changes_with_first_flipped += 1
        
        return min(changes_keeping_first, changes_with_first_flipped)
# @lc code=end

# 010
# 101

# 100
# 001
# 000
# 111

s = "0100"
sol = Solution()
# print(sol.minOperations(s))
# s = "1111"
# print(sol.minOperations(s))
s = "110010"
print(sol.minOperations(s))


from typing import *

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove all dashes and convert to uppercase
        s = s.replace('-', '').lower()
        
        # If the string is empty after removing dashes, return an empty string
        if not s:
            return ""
        
        # Calculate the length of the first group
        first_group_length = len(s) % k
        if first_group_length == 0:
            first_group_length = k
        
        # Initialize the result with the first group
        result = [s[:first_group_length]]
        
        # Add the remaining groups
        for i in range(first_group_length, len(s), k):
            result.append(s[i:i+k])
        
        # Join the groups with dashes
        return '-'.join(result).upper()

# Test the solution

solution = Solution()

print(
    solution.licenseKeyFormatting("5F3Z-2e-9-w", 4)
)
 
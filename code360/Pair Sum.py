from typing import List

def pairSum(arr: List[int], s: int):
    result = []
    # Loop through every unique pair (i, j) where i < j
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == s:
                result.append(sorted([arr[i], arr[j]]))  # Add the valid pair
    
    # Sort the result to return pairs in sorted order
    result.sort()
    return result

# Example test cases
print(pairSum([1, 2, 3, 4, 5], 5))
# Expected output: [[1, 4], [2, 3]]

print(pairSum([2, -3, 3, 3, -2], 0))
# Expected output: [[-3, 3], [-3, 3], [-2, 2]]


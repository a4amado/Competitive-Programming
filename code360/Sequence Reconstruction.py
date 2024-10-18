
from os import *
from sys import *
from collections import *
from math import *
from typing import *

from typing import List

def shortestSuperSeq(primary: List[int], secondary: List[List[int]], N: int, X: int, Y: int) -> bool:
    def is_subsequence(seq, superseq):
        it = iter(superseq)
        return all(c in it for c in seq)

    # Check if primary is a valid permutation of 1 to N
    if set(primary) != set(range(1, N + 1)):
        return False

    # Check if primary is a valid supersequence of all sequences in secondary
    if not all(is_subsequence(seq, primary) for seq in secondary):
        return False

    # Check if there's any other permutation that's also a valid supersequence
    for i in range(N - 1):
        for j in range(i + 1, N):
            # Create a new permutation by swapping two elements
            new_perm = primary[:]
            new_perm[i], new_perm[j] = new_perm[j], new_perm[i]
            
            # If this new permutation is also a valid supersequence, return False
            if all(is_subsequence(seq, new_perm) for seq in secondary):
                return False

    # If we've made it here, primary is the only valid shortest supersequence
    return True


# Test Case 1: Basic case where primary is the only shortest supersequence
def test_case_1():
    primary = [1, 2, 3, 4]
    secondary = [[1, 2], [2, 3], [3, 4]]
    N = 4
    X = 3  # Number of sequences in secondary
    Y = 2  # Maximum length of sequences in secondary
    expected_output = True
    result = shortestSuperSeq(primary, secondary, N, X, Y)
    assert result == expected_output, f"Test case 1 failed. Expected {expected_output}, but got {result}"

# Test Case 2: Primary is not the only shortest supersequence
def test_case_2():
    primary = [1, 2, 3]
    secondary = [[1, 2], [1, 3]]
    N = 3
    X = 2
    Y = 2
    expected_output = False
    result = shortestSuperSeq(primary, secondary, N, X, Y)
    assert result == expected_output, f"Test case 2 failed. Expected {expected_output}, but got {result}"

# Test Case 3: Primary is not a valid supersequence
def test_case_3():
    primary = [1, 2, 3, 4]
    secondary = [[1, 2], [3, 4], [2, 3]]
    N = 4
    X = 3
    Y = 2
    expected_output = False
    result = shortestSuperSeq(primary, secondary, N, X, Y)
    assert result == expected_output, f"Test case 3 failed. Expected {expected_output}, but got {result}"

# Test Case 4: All single-element sequences
def test_case_4():
    primary = [1, 2, 3, 4]
    secondary = [[1], [2], [3], [4]]
    N = 4
    X = 4
    Y = 1
    expected_output = True
    result = shortestSuperSeq(primary, secondary, N, X, Y)
    assert result == expected_output, f"Test case 4 failed. Expected {expected_output}, but got {result}"

# Test Case 5: One long sequence in secondary
def test_case_5():
    primary = [1, 2, 3, 4, 5]
    secondary = [[1, 2, 3, 4, 5]]
    N = 5
    X = 1
    Y = 5
    expected_output = True
    result = shortestSuperSeq(primary, secondary, N, X, Y)
    assert result == expected_output, f"Test case 5 failed. Expected {expected_output}, but got {result}"

# Test Case 6: Empty secondary
def test_case_6():
    primary = [1, 2, 3]
    secondary = []
    N = 3
    X = 0
    Y = 0
    expected_output = True
    result = shortestSuperSeq(primary, secondary, N, X, Y)
    assert result == expected_output, f"Test case 6 failed. Expected {expected_output}, but got {result}"

# Run all test cases
def run_all_tests():
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()
    print("All test cases passed!")

run_all_tests()

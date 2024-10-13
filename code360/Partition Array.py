from typing import List

def partitionArray(arr: List[int]) -> int:
    arr.sort()
    prefix = [0 for _ in range(len(arr))]
    prefix[0] = 0
    suffix =  [0 for _ in range(len(arr))]
    for idx in range(1, len(arr)):
        prefix[idx] = prefix[idx - 1] + arr[idx - 1]
    suffix[-1] = 0
    for idx in range(len(arr) - 2, -1, -1):
        suffix[idx] = suffix[idx + 1] + arr[idx + 1]
    print(prefix)
    print(suffix)

s = [8, 3, 1, 4, 9, 10]
print(partitionArray(s))

from os import *
from sys import *
from collections import *
from math import *


def findLCS(n: int, m: int, a: str, b: str) -> str:

	
    dp_table = [[0 for _ in range(len(a) +1 )] for _ in range(len(b)+ 1)]

    for i in range(1, len(dp_table)):
        for j in range(1, len(dp_table[0])):
            if a[j -1] == b[i -1]:
                dp_table[i][j] = dp_table[i -1][j -1]  + 1
            else:
                dp_table[i][j] = max(dp_table[i -1][j], dp_table[i][j -1])

    y, x = m,n

    s = []

    while y > 0 and x > 0:
        if b[y - 1] == a[x - 1]:
            s.append(b[y-1])
            y,x = y-1,x-1
            continue

        above = (dp_table[y-1][x], (y-1, x))
        left = (dp_table[y][x-1], (y,x-1))

        nextItem = max(above, left)
        y = nextItem[1][0]
        x = nextItem[1][1]

    return "".join(reversed(s))


str1 = "ABCBDAB"
str2 = "BDCABA"



print(
    findLCS(0,0,str1, str2)
)

str1 = "brute" 
str2  = "groot"


print(
    findLCS(0,0,str1, str2)
)
str1 = "ababa"
str2  = "cbbcad"



print(
    findLCS(0,0,str1, str2)
)
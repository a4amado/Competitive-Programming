from typing import *
from collections import Counter
from itertools import groupby

class Solution:

            
    def expressiveWords(self, word: str, words: List[str]) -> int:



        ss = ["".join(group) for char, group in groupby(word)]

        count = 0
        for word in words:

            compareTo = ["".join(group) for char, group in groupby(word)]
            if len(compareTo) != len(ss):continue
            
            validSegments = 0

            for idx in range(len(compareTo)):
                if compareTo[idx][0] != ss[idx][0]:break
                if len(ss[idx]) < len(compareTo[idx]):break
                if len(ss[idx]) < 3:
                    if len(ss[idx]) != len(compareTo[idx]):break
                    
                validSegments += 1
            if validSegments == len(compareTo):
                count += 1
        return count
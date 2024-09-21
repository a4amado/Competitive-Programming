from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return[newInterval]
            
        result = []
        i = 0
        n = len(intervals)
        
        result = []

        # append that ca be appended
        # append that ca be appended
        while i < n and intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
                i += 1
        #  
        while i < n and intervals[i][0] <= newInterval[1]:
            
            currInterval = intervals[i]
            
            newInterval =  [
                min(currInterval[0], newInterval[0]),
                max(currInterval[1], newInterval[1])
            ]

            
            i+=1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i+=1
        return result        

s = Solution()
print(s.insert([[1,5]], [2,3]))
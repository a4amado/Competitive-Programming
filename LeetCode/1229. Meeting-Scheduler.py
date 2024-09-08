"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)

        days = [intervals[0].end]

        for i in intervals[1:]:
            if i.start >= min(days):
                days[days.index(min(days))] = i.end
            else:
                return False
        return True
        
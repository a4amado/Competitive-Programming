class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        
        # List to keep track of end times for each day
        days = [intervals[0].end]
        
        for interval in intervals[1:]:
            # Check if the interval can be scheduled on an existing day
            if interval.start >= min(days):
                # Update the earliest ending day
                days[days.index(min(days))] = interval.end
            else:
                # If it can't be scheduled on any existing day, start a new day
                days.append(interval.end)
        
        return len(days)
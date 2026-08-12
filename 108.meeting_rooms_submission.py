"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n <= 1:
            return True
        
        intervals.sort(key=lambda x: x.start)
        i = 1
        while i < n:
            prevInterval = intervals[i - 1]
            curInterval = intervals[i]
            if prevInterval.end > curInterval.start:
                return False
            i += 1
        
        return True
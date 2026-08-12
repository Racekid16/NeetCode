"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # basically asking: max overlap?
        n = len(intervals)
        if n <= 1:
            return n

        times = []
        for interval in intervals:
            times.append([interval.start, "s"])
            times.append([interval.end, "e"])
        
        times.sort()
    
        res = 0
        count = 0
        for time in times:
            if time[1] == "s":
                count += 1
            else:
                count -= 1
            res = max(res, count)

        return res
        
        
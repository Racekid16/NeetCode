class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0
        
        intervals.sort(key=lambda x: x[0])

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:    # intervals don't overlap
                prevEnd = end
            # intervals overlap; remove one whose end is later
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        return res
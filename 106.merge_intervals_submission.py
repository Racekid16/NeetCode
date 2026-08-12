class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])

        res = []

        i = 0
        while i < n:
            curInterval = [intervals[i][0], intervals[i][1]]
            i += 1
            while i < n and curInterval[1] >= intervals[i][0]:
                curInterval[1] = max(curInterval[1], intervals[i][1])
                i += 1
            res.append(curInterval)
        
        return res
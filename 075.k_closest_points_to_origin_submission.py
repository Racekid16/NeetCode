import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            heapq.heappush(pq, (point[0] * point[0] + point[1] * point[1], point))
        
        res = []
        i = k
        while len(pq) > 0 and i > 0:
            res.append(heapq.heappop(pq)[1])
            i -= 1
        
        return res
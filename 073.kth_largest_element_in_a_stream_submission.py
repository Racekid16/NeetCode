import heapq

# explanation: 
# make heap only include the K largest elements
# because you can pop/retrieve the smallest elements efficiently
# and previously added elements cannot be removed
# so once an element is not one of the K largest elements
# it can never be the Kth largest element in the future
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

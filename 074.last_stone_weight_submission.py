import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesPq = [-stone for stone in stones]
        heapq.heapify(stonesPq)

        while len(stonesPq) > 1:
            heaviestStone = heapq.heappop(stonesPq)
            secondHeaviestStone = heapq.heappop(stonesPq)

            if heaviestStone == secondHeaviestStone:
                continue
            # else heaviestStone > secondHeaviestStone
            heapq.heappush(stonesPq, heaviestStone - secondHeaviestStone)

        if len(stonesPq) == 0:
            return 0
        
        return stonesPq[0] * -1
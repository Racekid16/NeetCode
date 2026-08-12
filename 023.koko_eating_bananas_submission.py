class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        # nlog(m) suggests:
        # - we need to lootestEatingRate at each of the n piles in piles
        # - we need to testEatingRateeep splitting the largest pile of size m in half
        #   - we should probably do one pass (O(n)) to find the largest pile

        m = -1
        for pileIndex in range(n):
            if piles[pileIndex] > m:
                m = piles[pileIndex]
        
        # m is now the size of the largest pile
        maxPossibleEatingRate = m
        minPossibleEatingRate = 1

        minEatingRate = maxPossibleEatingRate

        while minPossibleEatingRate <= maxPossibleEatingRate:
            numHours = 0
            testEatingRate = (minPossibleEatingRate + maxPossibleEatingRate) // 2

            for pileIndex in range(n):
                numHours += math.ceil(piles[pileIndex] / testEatingRate)
            
            if numHours > h:
                # testEatingRate is too low
                minPossibleEatingRate = testEatingRate + 1
            
            elif numHours <= h:  
                minEatingRate = min(minEatingRate, testEatingRate)
                # testEatingRate is possibly too high
                maxPossibleEatingRate = testEatingRate - 1
            
        return minEatingRate
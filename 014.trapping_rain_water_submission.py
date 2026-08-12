class Solution:
    def trap(self, height: List[int]) -> int:
        # water at specific X =
        # max(
        #   min(maxHeight left of X, maxHeight right of X) - height at X,
        #   0
        # )
        if len(height) < 3:
            return 0

        maxHeightLeftOfX = [0 for _ in range(len(height))]
        maxHeightRightOfX = [0 for _ in range(len(height))]

        for x in range(1, len(height), 1):
            maxHeightLeftOfX[x] = max(maxHeightLeftOfX[x - 1], height[x - 1])

        for x in range(len(height) - 2, -1, -1):
            maxHeightRightOfX[x] = max(maxHeightRightOfX[x + 1], height[x + 1])
        
        totalWater = 0

        for x in range(len(height)):
            totalWater += max(min(maxHeightLeftOfX[x], maxHeightRightOfX[x]) - height[x], 0)
        
        return totalWater
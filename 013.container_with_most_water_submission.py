class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(heights) - 1
        maxArea = -1

        while leftPtr < rightPtr:
            leftHeight = heights[leftPtr]
            rightHeight = heights[rightPtr]

            containerHeight = min(leftHeight, rightHeight)
            containerWidth = rightPtr - leftPtr

            containerArea = containerWidth * containerHeight

            if containerArea > maxArea:
                maxArea = containerArea
            
            if leftHeight == rightHeight:
                leftPtr += 1
                rightPtr -= 1
            
            if leftHeight < rightHeight:
                leftPtr += 1
            
            if rightHeight < leftHeight:
                rightPtr -= 1
        
        return maxArea


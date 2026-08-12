class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        largestArea = -1

        # to know the area of a rectangle, you need to know:
        # - how many units away the left side of the rectangle is from the right side
        #   of the rectangle (rightBarIndex - leftBarIndex + 1)
        # - the minimum height of all bars in that span

        # for a given barIndex, if heights[barIndex] is the height of the rectangle,
        # what is the width of the rectangle that maximizes that rectangle's area?
        # Ans: keep going left until you reach a bar that is shorter;
        # keep going right until you reach a bar that is shorter;
        # width is (numBarsLeftTilShorter - 1) + 1 + (numBarsRightTilShorter - 1).

        # this stack is a stack of bar indices
        # whose numBarsRightTilShorter still needs to be determined
        stack = []
        numBarsRightTilShorter = [n - barIndex for barIndex in range(n)]
        for barIndex in range(n):
            while len(stack) > 0 and heights[stack[-1]] > heights[barIndex]:
                numBarsRightTilShorter[stack[-1]] = barIndex - stack[-1]
                stack.pop()
            stack.append(barIndex)

        # this stack is a stack of bar indices
        # whose numBarsLeftTilShorter still needs to be determined
        stack = []
        numBarsLeftTilShorter = [barIndex + 1 for barIndex in range(n)]
        for barIndex in range(n - 1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] > heights[barIndex]:
                numBarsLeftTilShorter[stack[-1]] = stack[-1] - barIndex
                stack.pop()
            stack.append(barIndex)
        
        for barIndex in range(n):
            thisRectangleWidth = (numBarsLeftTilShorter[barIndex] - 1) \
                               + 1 \
                               + (numBarsRightTilShorter[barIndex] - 1)
            thisRectangleHeight = heights[barIndex]
            thisRectangleArea = thisRectangleWidth * thisRectangleHeight

            if thisRectangleArea > largestArea:
                largestArea = thisRectangleArea

        return largestArea
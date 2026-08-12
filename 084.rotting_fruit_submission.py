class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        numRows = len(grid)
        numCols = len(grid[0])
        numFresh = 0
        numMins = 0
        q = deque()
        
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 1:
                    numFresh += 1
                if grid[row][col] == 2:
                    q.append((row, col, 0))
        
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while len(q) > 0 and numFresh > 0:
            row, col, time = q.popleft()
            
            for offset in offsets:
                newRow = row + offset[0]
                newCol = col + offset[1]

                if (
                    newRow < 0 or newRow > numRows - 1 or
                    newCol < 0 or newCol > numCols - 1 or
                    grid[newRow][newCol] != 1
                ):
                    continue
                
                grid[newRow][newCol] = 2
                q.append((newRow, newCol, time + 1))
                numFresh -= 1
                numMins = time + 1
        
        if numFresh != 0:
            return -1

        return numMins

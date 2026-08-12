from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647 
        numRows = len(grid)
        numCols = len(grid[0])

        q = deque()

        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
        
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while len(q) > 0:
            row, col, dist = q.popleft()
            if grid[row][col] != 0 and grid[row][col] != INF:
                continue
            grid[row][col] = dist

            for offset in offsets:
                newRow = row + offset[0]
                newCol = col + offset[1]
                if (
                    newRow < 0 or newRow > numRows - 1 or
                    newCol < 0 or newCol > numCols - 1 or
                    grid[newRow][newCol] != INF
                ):
                    continue
                
                q.append((newRow, newCol, dist + 1))
        
        # no return value

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        maxArea = 0
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row, col):
            q = deque()
            visited[row][col] = True
            q.append((row, col))
            res = 0

            while len(q) > 0:
                (r, c) = q.popleft()
                res += 1
                for offset in offsets:
                    newRow = r + offset[0]
                    newCol = c + offset[1]
                    if (
                        newRow < 0 or newRow > numRows - 1 or
                        newCol < 0 or newCol > numCols - 1 or
                        grid[newRow][newCol] != 1 or 
                        visited[newRow][newCol] 
                    ):
                        continue
                    visited[newRow][newCol] = True
                    q.append((newRow, newCol))
            
            return res
        
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == 1 and not visited[row][col]:
                    area = bfs(row, col)
                    maxArea = max(area, maxArea)

        return maxArea
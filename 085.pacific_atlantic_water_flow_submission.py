class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        numRows = len(heights)
        numCols = len(heights[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = [[False for _ in range(numCols)] for _ in range(numRows)]
        atlantic = [[False for _ in range(numCols)] for _ in range(numRows)]

        def bfs(source, ocean):
            q = deque(source)

            for row, col in source:
                ocean[row][col] = True

            while q:
                row, col = q.popleft()

                for dr, dc in offsets:
                    newRow = row + dr
                    newCol = col + dc
                    
                    if (
                        newRow < 0 or newRow >= numRows or
                        newCol < 0 or newCol >= numCols or
                        ocean[newRow][newCol] or
                        heights[newRow][newCol] < heights[row][col]
                    ):
                        continue
                    
                    ocean[newRow][newCol] = True
                    q.append((newRow, newCol))

        pacificSources = []
        atlanticSources = []

        for row in range(numRows):
            pacificSources.append((row, 0))
            atlanticSources.append((row, numCols - 1))

        for col in range(numCols):
            pacificSources.append((0, col))
            atlanticSources.append((numRows - 1, col))

        bfs(pacificSources, pacific)
        bfs(atlanticSources, atlantic)

        res = []

        for row in range(numRows):
            for col in range(numCols):
                if pacific[row][col] and atlantic[row][col]:
                    res.append([row, col])

        return res
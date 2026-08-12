class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        visited = [[False for _ in range(numCols)] for _ in range(numRows)]
        numIslands = 0

        def dfs(row, col):
            if (
                row < 0 or row > numRows - 1 or
                col < 0 or col > numCols - 1 or
                grid[row][col] != "1" or
                visited[row][col] == True
            ):
                return
            visited[row][col] = True
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        for row in range(numRows):
            for col in range(numCols):
                if grid[row][col] == "1" and not visited[row][col]:
                    numIslands += 1
                    dfs(row, col)

        return numIslands
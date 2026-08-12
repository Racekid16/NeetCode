class Solution:
    def solve(self, board: List[List[str]]) -> None:
        numRows = len(board)
        numCols = len(board[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(s):
            for (row, col) in s:
                board[row][col] = "#"

            while len(s) > 0:
                (row, col) = s.pop()

                for (dr, dc) in offsets:
                    newRow = row + dr
                    newCol = col + dc

                    if (
                        newRow < 0 or newRow > numRows - 1 or
                        newCol < 0 or newCol > numCols - 1 or
                        board[newRow][newCol] != "O"
                    ):
                        continue
                    board[newRow][newCol] = "#"
                    s.append((newRow, newCol))

        borderTiles = []

        for row in [0, numRows - 1]:
            for col in range(numCols):
                if board[row][col] == "O":
                    borderTiles.append((row, col))
        
        for col in [0, numCols - 1]:
            for row in range(1, numRows - 1, 1):
                if board[row][col] == "O":
                    borderTiles.append((row, col))
        
        dfs(borderTiles)

        for row in range(numRows):
            for col in range(numCols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"

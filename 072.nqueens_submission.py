class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        occupiedColInRows = [-1 for _ in range(n)]
        occupiedCols = [False for _ in range(n)]
        occupiedLeftDiagonals = [False for _ in range(2 * n - 1)]
        occupiedRightDiagonals = [False for _ in range(2 * n - 1)]

        def placeQueen(row):
            if row == n:
                board = []
                for r in range(n):
                    boardRow = ""
                    for c in range(n):
                        if occupiedColInRows[r] == c:
                            boardRow += "Q"
                        else:
                            boardRow += "."
                    board.append(boardRow)
                res.append(board)
                return

            for col in range(n):
                leftDiagonalIndex = row + col
                rightDiagonalIndex = n - 1 + row - col

                if occupiedCols[col] \
                or occupiedLeftDiagonals[leftDiagonalIndex] \
                or occupiedRightDiagonals[rightDiagonalIndex]:
                    continue

                occupiedColInRows[row] = col
                occupiedCols[col] = True
                occupiedLeftDiagonals[leftDiagonalIndex] = True
                occupiedRightDiagonals[rightDiagonalIndex] = True

                placeQueen(row + 1)

                occupiedRightDiagonals[rightDiagonalIndex] = False
                occupiedLeftDiagonals[leftDiagonalIndex] = False
                occupiedCols[col] = False
                occupiedColInRows[row] = -1

        placeQueen(0)
        return res

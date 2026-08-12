class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            # True at index i means number i + 1 is present in this row
            rowNumCounts = [False for _ in range(9)]

            for col in range(9):
                gridVal = board[row][col]

                if gridVal == ".":
                    continue
    
                if rowNumCounts[int(gridVal) - 1] == True:
                    return False
        
                rowNumCounts[int(gridVal) - 1] = True
        
        for col in range(9):
            # True at index i means number i is present in this col
            colNumCounts = [False for _ in range(9)]

            for row in range(9):
                gridVal = board[row][col]

                if gridVal == ".":
                    continue
                
                if colNumCounts[int(gridVal) - 1] == True:
                    return False
                
                colNumCounts[int(gridVal) - 1] = True

        for subBoxRow in range(3):
            for subBoxCol in range(3):
                subBoxNumCounts = [False for _ in range(9)]

                for row in range(subBoxRow * 3, subBoxRow * 3 + 3, 1):
                    for col in range(subBoxCol * 3, subBoxCol * 3 + 3, 1):
                        gridVal = board[row][col]

                        if gridVal == ".":
                            continue
                        
                        if subBoxNumCounts[int(gridVal) - 1] == True:
                            return False
                        
                        subBoxNumCounts[int(gridVal) - 1] = True
        
        return True
                        

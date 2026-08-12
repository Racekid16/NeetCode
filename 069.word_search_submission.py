class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row, col, currLen):
            if currLen == len(word):
                return True

            if row < 0 or row >= len(board) \
            or col < 0 or col >= len(board[0]) \
            or board[row][col] != word[currLen]:
                return False

            tmp = board[row][col]
            board[row][col] = "*"

            found = (
                dfs(row - 1, col, currLen + 1) or
                dfs(row + 1, col, currLen + 1) or
                dfs(row, col - 1, currLen + 1) or
                dfs(row, col + 1, currLen + 1) 
            )
            
            board[row][col] = tmp

            return found
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        
        return False
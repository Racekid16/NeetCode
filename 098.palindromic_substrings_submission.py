class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        numPalindromes = 0

        # memo[i][j] == True if s[i:j+1] is a palindrome; False otherwise
        memo = [[False for _ in range(n)] for _ in range(n)]
        
        # recursive case: s[i:j+1] is a palindrome if s[i] == s[j]
        # and s[i+1:j] is a palindrome (for j >= i + 2)
        # increase start -> go down a row
        # decrease end -> go left a column

        # tip: if the current cell needs the cell below it,
        # iterate through the rows backward
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or memo[i + 1][j - 1] == True):
                    memo[i][j] = True
                    numPalindromes += 1
        
        return numPalindromes

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(curr, i):
            if i >= len(s):
                res.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    curr.append(s[i:j+1])
                    dfs(curr, j + 1)
                    curr.pop()
        
        dfs([], 0)

        return res
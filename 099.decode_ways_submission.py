class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1 for _ in range(n + 1)]

        # number of ways to decode the first i characters of s
        # consider the test cases where the last 2 characters are:
        # - "22"
        # - "20"
        # - "00"
        # what does this function return in each case?
        def helper(i):
            if i == 0:
                return 1

            if memo[i] != -1:
                return memo[i]
            
            res = 0
            if s[i - 1] != '0':
                res += helper(i - 1)

            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                res += helper(i - 2)

            memo[i] = res
            return memo[i]

        return helper(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for _ in range(n + 1)]

        # the number of ways to get to step i
        def helper(i):
            if i == 0 or i == 1:
                return 1
            if memo[i] != -1:
                return memo[i]
            memo[i] = helper(i - 1) + helper(i - 2)
            return memo[i]
        
        return helper(n)

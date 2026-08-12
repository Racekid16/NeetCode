class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # memo[i] is the minimum cost to reach step i
        memo = [-1 for _ in range(n + 1)]

        # the minimum cost to reach step
        def helper(step):
            if step == 0 or step == 1:
                return 0

            if memo[step] != -1:
                return memo[step]
            
            memo[step] = min(helper(step - 2) + cost[step - 2], helper(step - 1) + cost[step - 1])
            return memo[step]
        
        return helper(n)
        
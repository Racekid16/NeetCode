class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo[i] = the maximum amount you can steal by robbing the first i houses
        n = len(nums)
        memo = [-1 for _ in range(n + 1)]

        def helper(i):
            if i == 0:
                return 0
            
            if i == 1:
                return nums[0]
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(helper(i - 2) + nums[i - 1], helper(i - 1))
            return memo[i]
        
        return helper(n)
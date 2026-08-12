class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # memo[i] is the length of the longest increasing subsequence ending at index i
        memo = [1 for _ in range(len(nums))]
        maxLen = 1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)
                    maxLen = max(maxLen, memo[i])

        return maxLen
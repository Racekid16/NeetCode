class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # maxProd[i] is the maximum product of any subarray ending at nums[i]
        maxProd = [None for _ in range(n)]
        minProd = [None for _ in range(n)]

        maxProd[0] = 1 if nums[0] == 0 else nums[0]
        minProd[0] = 1 if nums[0] == 0 else nums[0]

        globalMax = nums[0]

        for i in range(1, n):
            if nums[i] == 0:
                maxProd[i] = 1
                minProd[i] = 1
                globalMax = max(globalMax, 0)
            else:
                maxProd[i] = max(nums[i], nums[i] * maxProd[i - 1], nums[i] * minProd[i - 1])
                minProd[i] = min(nums[i], nums[i] * maxProd[i - 1], nums[i] * minProd[i - 1])
                globalMax = max(globalMax, maxProd[i])

        return globalMax

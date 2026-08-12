class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        totalSum = sum(nums)
        
        if totalSum % 2 != 0:
            return False
        
        targetSum = totalSum / 2
        memo = {}  # (i, subsetSum) -> bool
        
        def genSubsets(i, subsetSum):
            if i == n or subsetSum > targetSum:
                return False
            
            if (i, subsetSum) in memo:
                return memo[(i, subsetSum)]
            
            if subsetSum == targetSum:
                return True
            
            result = genSubsets(i + 1, subsetSum + nums[i]) or genSubsets(i + 1, subsetSum)
            memo[(i, subsetSum)] = result
            return result
        
        return genSubsets(0, 0)

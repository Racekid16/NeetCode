import json

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(currNums, smallestIndex, currSum):
            if currSum == target:
                res.append(currNums.copy())
                return
            
            if currSum > target:
                return
            
            for i in range(smallestIndex, len(nums), 1):
                num = nums[i]
                currNums.append(num)
                backtrack(currNums, i, currSum + num)
                currNums.pop()
        
        backtrack([], 0, 0)

        return res

        
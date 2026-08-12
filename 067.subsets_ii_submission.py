class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(curr, currIndex):
            if currIndex == len(nums):
                res.append(curr.copy())
                return
            
            # include number
            curr.append(nums[currIndex])
            backtrack(curr, currIndex + 1)
            curr.pop()

            while currIndex + 1 < len(nums) \
            and nums[currIndex] == nums[currIndex + 1]:
                currIndex += 1

            # don't include number
            backtrack(curr, currIndex + 1)

        backtrack([], 0)
        return res
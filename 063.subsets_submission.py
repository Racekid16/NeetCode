class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number: can either include it or not
        subsets = []

        def backtrack(currSubset, currIndex):
            if currIndex == len(nums):
                subsets.append(currSubset.copy())
                return
            
            # don't include number
            backtrack(currSubset, currIndex + 1)

            # include number
            currSubset.append(nums[currIndex])
            backtrack(currSubset, currIndex + 1)
            currSubset.pop()

        backtrack([], 0)
        return subsets
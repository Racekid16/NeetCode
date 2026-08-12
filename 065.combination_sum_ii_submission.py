class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(currNums, smallestIndex, currSum):
            if currSum == target:
                res.append(currNums.copy())
                return
            for i in range(smallestIndex, len(candidates), 1):
                if i > smallestIndex and candidates[i] == candidates[i - 1]:
                    continue
                num = candidates[i]
                if currSum + num > target:
                    break
                currNums.append(num)
                backtrack(currNums, i + 1, currSum + num)
                currNums.pop()
        
        backtrack([], 0, 0)

        return res

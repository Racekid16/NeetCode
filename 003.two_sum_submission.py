class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listNumIndex = dict()

        for numIndex in range(len(nums)):
            numValue = nums[numIndex]
            otherNumValue = target - numValue

            if otherNumValue in listNumIndex:
                otherNumIndex = listNumIndex[otherNumValue]
                return [otherNumIndex, numIndex]

            listNumIndex[numValue] = numIndex

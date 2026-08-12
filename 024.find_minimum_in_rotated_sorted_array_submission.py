class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1

        # edge case: len(nums) == 1 or nums functionally has no rotation
        if nums[leftIndex] <= nums[rightIndex]:
            return nums[leftIndex]

        # otherwise, nums has a rotation.
        while leftIndex < rightIndex:
            midIndex = (leftIndex + rightIndex) // 2

            midVal = nums[midIndex]
            rightVal = nums[rightIndex]

            # minIndex is strictly to the right of midIndex
            if midVal > rightVal:
                leftIndex = midIndex + 1
            # minIndex is at midIndex or to the left of midIndex
            else:
                rightIndex = midIndex

        # leftIndex == rightIndex; leftIndex is minIndex
        return nums[leftIndex]

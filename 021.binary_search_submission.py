class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1

        leftPtr = 0
        rightPtr = n

        while leftPtr <= rightPtr:
            midIndex = leftPtr + ((rightPtr - leftPtr) // 2)

            if nums[midIndex] > target:
                rightPtr = midIndex - 1
            
            elif nums[midIndex] < target:
                leftPtr = midIndex + 1
            
            else:
                return midIndex

        return -1
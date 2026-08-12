class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        leftIndex = 0
        rightIndex = n - 1

        # Perform a binary search for target only in the specified region.
        # Requires: minIndex > 0, and nums[minIndex] < nums[maxIndex]
        # Modifies: 
        # Effects: returns the index that target is at if it is within the specified region,
        # else returns -1
        def binarySearch(minIndex: int, maxIndex: int) -> int:
            leftIndex = minIndex
            rightIndex = maxIndex

            while leftIndex <= rightIndex:
                midIndex = (leftIndex + rightIndex) // 2

                if nums[midIndex] == target:
                    return midIndex
                
                elif nums[midIndex] < target:
                    # target is strictly to the right of midIndex, if it exists
                    leftIndex = midIndex + 1
                
                else: # nums[midIndex] > target:
                    # target is strictly to the left of midIndex, if it exists
                    rightIndex = midIndex - 1

            return -1

        # find inflection point
        # after while loop exits, nums[leftIndex] should be the minimum value in nums
        while leftIndex < rightIndex:
            midIndex = (leftIndex + rightIndex) // 2

            midVal = nums[midIndex]
            rightVal = nums[rightIndex]

            # case: midIndex is in left segment
            if midVal > rightVal:
                # minVal is strictly to the right of midIndex
                leftIndex = midIndex + 1

            # case: midIndex is in right segment
            else:   # midVal <= rightVal
                # minVal is at or to the left of midIndex
                rightIndex = midIndex

        # leftIndex == rightIndex; 
        # nums[leftIndex] = minVal
        if leftIndex == 0:  
            # array not rotated, just search whole thing
            return binarySearch(0, n - 1)

        # target must be in left segment, if it exists
        elif target >= nums[0] and target <= nums[leftIndex - 1]:
            return binarySearch(0, leftIndex - 1)
        
        # else target must be in right segment, if it exists
        return binarySearch(leftIndex, n - 1)

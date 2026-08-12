class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m <= n:
            shorterList = nums1
            longerList = nums2
            shorterListLen = m
            longerListLen = n
        else:
            shorterList = nums2
            longerList = nums1
            shorterListLen = n
            longerListLen = m

        half = (m + n + 1) // 2  # left partition gets extra element if odd

        # handle case where shorterList is empty
        if shorterListLen == 0:
            if (m + n) % 2 == 1:
                return longerList[half - 1]
            return (longerList[half - 1] + longerList[half]) / 2

        leftIndex = 0
        rightIndex = shorterListLen

        # binary search on shorterList
        while leftIndex <= rightIndex:
            # the number of elements in the left partition of the shorter list
            shorterListPartition = (leftIndex + rightIndex) // 2
            # the number of elements in the left partition of the longer list
            longerListPartition = half - shorterListPartition

            if shorterListPartition == 0:
                shorterListLeftPartitionMax = float('-inf')
            else:
                shorterListLeftPartitionMax = shorterList[shorterListPartition - 1]

            if shorterListPartition == shorterListLen:
                shorterListRightPartitionMin = float('inf')
            else:
                shorterListRightPartitionMin = shorterList[shorterListPartition]


            if longerListPartition == 0:
                longerListLeftPartitionMax = float('-inf')
            else:
                longerListLeftPartitionMax = longerList[longerListPartition - 1]

            if longerListPartition == longerListLen:
                longerListRightPartitionMin = float('inf')
            else:
                longerListRightPartitionMin = longerList[longerListPartition]


            # check if valid partition
            if shorterListLeftPartitionMax <= longerListRightPartitionMin and \
               longerListLeftPartitionMax <= shorterListRightPartitionMin:

                if (m + n) % 2 == 1:
                    return max(shorterListLeftPartitionMax, longerListLeftPartitionMax)
                
                leftPartitionMax = max(shorterListLeftPartitionMax, longerListLeftPartitionMax)
                rightPartitionMin = min(shorterListRightPartitionMin, longerListRightPartitionMin)
                return (leftPartitionMax + rightPartitionMin) / 2

            # If the cut in shorterList is too far right, move it left.
            elif shorterListLeftPartitionMax > longerListRightPartitionMin:
                rightIndex = shorterListPartition - 1

            # If the cut in shorterList is too far left, move it right.
            else:   # longerListLeftPartitionMax > shorterListRightPartitionMin
                leftIndex = shorterListPartition + 1

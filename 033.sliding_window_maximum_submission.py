from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []

        # Properties of the queue:
        # - The queue only contains indices for elements currently in the window:
        #       leftNumIndex <= numsIndicesQueue[i] <= rightNumIndex
        #           for all integers 0 <= i < len(numsIndicesQueue)
        # - The queue stores indices in increasing order:
        #       numsIndicesQueue[i] < numsIndicesQueue[j]
        #           for all integers 0 <= i < j < len(numsIndicesQueue)
        # - The values of the elements pointed to by the indices in the queue are monotonically decreasing:
        #       nums[numsIndicesQueue[i]] > nums[numsIndicesQueue[j]]
        #           for all integers 0 <= i < j < len(numsIndicesQueue)
        # - numsIndicesQueue[0] == leftNumIndex
        #       if leftNumIndex in numIndicesQueue
        # - 0 <= len(numIndicesQueue) <= k
        # - nums[numsIndicesQueue[0]] is always the minimum value in the current window
        #       if windowLength == k
        numsIndicesQueue = deque()

        leftNumIndex = 0

        for rightNumIndex in range(n):
            # maintain decreasing order by values
            while len(numsIndicesQueue) > 0 and nums[rightNumIndex] > nums[numsIndicesQueue[-1]]:
                numsIndicesQueue.pop()

            numsIndicesQueue.append(rightNumIndex)
            windowLength = rightNumIndex - leftNumIndex + 1

            if windowLength == k:
                res.append(nums[numsIndicesQueue[0]])

                # if the leftmost index is leaving the window, remove it
                if numsIndicesQueue[0] == leftNumIndex:
                    numsIndicesQueue.popleft()

                leftNumIndex += 1

        return res

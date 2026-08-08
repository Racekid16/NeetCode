# Run with: python3 076.kth_largest_element_in_array.py 076.kth_largest_element_in_array_tests.txt

import sys
import ast
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: python3 {sys.argv[0]} <test_cases.txt>")
        sys.exit(1)

    sol = Solution()
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            args = ast.literal_eval(f"({line},)")
            result = sol.findKthLargest(*args)
            print(f"{line} -> {result}")

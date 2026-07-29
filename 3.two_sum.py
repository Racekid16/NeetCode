# Run with: python3 3.two_sum.py 3.two_sum_tests.txt

import sys
import ast
from typing import List


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

        # should never reach here
        return [0, 0]


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
            result = sol.twoSum(*args)
            print(f"{line} -> {result}")

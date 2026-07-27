# Run with: python3 1.contains_duplicate.py 1.contains_duplicate_tests.txt

import sys
import ast
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


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
            result = sol.hasDuplicate(*args)
            print(f"{line} -> {result}")

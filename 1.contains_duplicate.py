# Run with: python3 1.contains_duplicate.py 1.contains_duplicate_tests.json

import sys
import json
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: python3 {sys.argv[0]} <test_cases.json>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        test_cases = json.load(f)

    sol = Solution()
    for case in test_cases:
        result = sol.hasDuplicate(case)
        print(f"{case} -> {result}")

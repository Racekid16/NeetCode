from typing import List
import sys
import json


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"usage: python3 {sys.argv[0]} <test_cases.txt>")
        sys.exit(1)

    sol = Solution()
    with open(sys.argv[1]) as f:
        cases = json.load(f)

    passed = 0
    for i, case in enumerate(cases):
        actual = sol.hasDuplicate(**case["input"])
        expected = case["output"]
        ok = actual == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] case {i}: input={case['input']} expected={expected} actual={actual}"
        )

    print(f"\n{passed}/{len(cases)} passed")
    sys.exit(0 if passed == len(cases) else 1)

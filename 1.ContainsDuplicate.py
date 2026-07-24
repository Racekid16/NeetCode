# Example usage: python3 1.ContainsDuplicate.py 1 2 3 3

import sys
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

if __name__ == "__main__":
    nums = [int(x) for x in sys.argv[1:]]
    print(Solution().hasDuplicate(nums))

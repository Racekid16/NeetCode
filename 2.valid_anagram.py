# Run with: python3 1.valid_anagram.py 1.valid_anagram_tests.txt

import sys
import ast


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterCounts = dict()

        for letter in s:
            letterCounts[letter] = letterCounts.get(letter, 0) + 1

        for letter in t:
            try:
                letterCounts[letter] -= 1

                if letterCounts[letter] == 0:
                    del letterCounts[letter]

            except:
                return False

        return len(letterCounts.keys()) == 0


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
            result = sol.isAnagram(*args)
            print(f"{line} -> {result}")

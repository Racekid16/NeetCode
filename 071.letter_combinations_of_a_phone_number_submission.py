class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(curr, currIndex):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for char in mappings[digits[currIndex]]:
                dfs(curr + char, currIndex + 1)
        
        if len(digits) > 0:
            dfs("", 0)
        
        return res
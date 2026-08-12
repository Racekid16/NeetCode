class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # memo[i] = True if first i chars of s can be segmented; False otherwise
        memo = [None for _ in range(n + 1)]

        def helper(i):
            if i == 0:
                return True
            
            if memo[i] != None:
                return memo[i]
            
            for word in wordDict:
                wordLen = len(word)
                if i >= wordLen and s[i - wordLen : i] == word and helper(i - wordLen) == True:
                    memo[i] = True
                    return memo[i]
            
            memo[i] = False
            return memo[i]
            
        return helper(n)
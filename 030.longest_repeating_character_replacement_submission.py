class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        longestSubstringLen = 0

        leftCharIndex = 0
        # key is character, value is how many times the char appears
        # in the current substirng
        charCounts = {}
        highestCharCount = 0

        for rightCharIndex in range(n):
            charCounts[s[rightCharIndex]] = 1 + charCounts.get(s[rightCharIndex], 0)
            highestCharCount = max(highestCharCount, charCounts[s[rightCharIndex]])

            while (rightCharIndex - leftCharIndex + 1) - highestCharCount > k:
                charCounts[s[leftCharIndex]] -= 1
                leftCharIndex += 1
            
            thisSubstringLen = rightCharIndex - leftCharIndex + 1
            longestSubstringLen = max(longestSubstringLen, thisSubstringLen)

        return longestSubstringLen
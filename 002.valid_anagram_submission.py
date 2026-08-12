class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sLetterCounts = dict()
        tLetterCounts = dict()

        for letterIndex in range(len(s)):
            sLetter = s[letterIndex]
            sLetterCounts[sLetter] = sLetterCounts.get(sLetter, 0) + 1

            tLetter = t[letterIndex]
            tLetterCounts[tLetter] = tLetterCounts.get(tLetter, 0) + 1
        
        for sLetterKey in sLetterCounts:
            if sLetterCounts[sLetterKey] != tLetterCounts.get(sLetterKey, -1):
                return False
        
        return True
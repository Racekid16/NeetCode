class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        shortestSubstring = ""

        # index is a character A-Za-z mapped to a number,
        # value is number of times character appears in the string
        tCharCounts = [0 for _ in range(52)]
        substringCharCounts = [0 for _ in range(52)]

        # Requires: a single lowercase or uppercase character
        # Returns: an integer index in [0, 52) used for indexing into tCharCounts
        # and substringCharCounts
        def mapCharToIndex(c: str) -> int: 
            if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                return ord(c) - ord("A")
            elif c in "abcdefghijklmnopqrstuvwxyz":
                return ord(c) - ord("a") + 26
            raise Exception("c must be a lowercase or uppercase character!")

        # Returns: whether all characters in t appear at least as many times in substring
        def tCharsInSubstring():
            for i in range(52):
                if substringCharCounts[i] < tCharCounts[i]:
                    return False
            return True

        for char in t:
            tCharCounts[mapCharToIndex(char)] += 1

        leftCharIndex = 0
        rightCharIndex = 0

        # idea: move rightCharIndex right until window contains t. 
        # then move leftCharIndex right until window doesn't contain t.
        # then record shortest substring.
        while leftCharIndex < n:
            while rightCharIndex < n and not tCharsInSubstring():
                substringCharCounts[mapCharToIndex(s[rightCharIndex])] += 1
                rightCharIndex += 1

            if tCharsInSubstring():
                thisSubstringLen = rightCharIndex - leftCharIndex
                if shortestSubstring == "" or thisSubstringLen < len(shortestSubstring):
                    shortestSubstring = s[leftCharIndex : rightCharIndex]

            substringCharCounts[mapCharToIndex(s[leftCharIndex])] -= 1
            leftCharIndex += 1

        return shortestSubstring

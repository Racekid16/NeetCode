class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        # the current window we're examining
        # should always have no duplicate characters
        charsInWindow = set()
        longestSubstringLen = 0

        leftCharIndex = 0
        rightCharIndex = 0

        while leftCharIndex < n and rightCharIndex < n:
            # with the current leftCharIndex, see how far right you can stretch the window
            while rightCharIndex < n and s[rightCharIndex] not in charsInWindow:
                charsInWindow.add(s[rightCharIndex])
                rightCharIndex += 1
            
            # the current window is [leftCharIndex, rightCharIndex - 1]
            # we cannot stretch this window right any more.
            # this is the longest substring starting at leftCharIndex with unique characters
            longestSubstringLen = max(longestSubstringLen, len(charsInWindow))
            
            charsInWindow.remove(s[leftCharIndex])
            leftCharIndex += 1
        
        return longestSubstringLen
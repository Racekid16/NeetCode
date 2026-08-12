class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1LetterCounts = [0 for _ in range(26)]
        for letter in s1:
            s1LetterCounts[ord(letter) - ord("a")] += 1
        
        substringLetterCounts = [0 for _ in range(26)]
        for letter in s2[:len(s1)]:
            substringLetterCounts[ord(letter) - ord("a")] += 1

        # count how many letters currently match between s1 and the window
        matches = 0
        for i in range(26):
            if s1LetterCounts[i] == substringLetterCounts[i]:
                matches += 1

        for letterIndex in range(len(s2) - len(s1)):
            if matches == 26:
                return True

            # character leaving the window (leftmost)
            firstLetterCountIndex = ord(s2[letterIndex]) - ord("a")

            # update for the outgoing letter
            substringLetterCounts[firstLetterCountIndex] -= 1
            if s1LetterCounts[firstLetterCountIndex] == substringLetterCounts[firstLetterCountIndex]:
                matches += 1
            elif s1LetterCounts[firstLetterCountIndex] == substringLetterCounts[firstLetterCountIndex] + 1:
                matches -= 1

            # character entering the window (new rightmost)
            lastLetterCountIndex = ord(s2[letterIndex + len(s1)]) - ord("a")
            # update for the incoming letter
            
            substringLetterCounts[lastLetterCountIndex] += 1
            if s1LetterCounts[lastLetterCountIndex] == substringLetterCounts[lastLetterCountIndex]:
                matches += 1
            elif s1LetterCounts[lastLetterCountIndex] == substringLetterCounts[lastLetterCountIndex] - 1:
                matches -= 1

        return matches == 26

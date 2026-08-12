class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPtr = 0
        rightPtr = len(s) - 1

        validChars = "abcdefghijklmnopqrstuvwxyz0123456789"

        while leftPtr < rightPtr:
            leftChar = s[leftPtr].lower()
            rightChar = s[rightPtr].lower()

            while leftPtr < rightPtr and leftChar not in validChars:
                leftPtr += 1
                leftChar = s[leftPtr].lower()
            
            while leftPtr < rightPtr and rightChar not in validChars:
                rightPtr -= 1
                rightChar = s[rightPtr].lower()
            
            if leftChar != rightChar:
                return False
            
            leftPtr += 1
            rightPtr -= 1
            
        return True
            
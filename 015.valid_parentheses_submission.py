class Solution:
    def isValid(self, s: str) -> bool:
        charStack = []
        openCloseDict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for char in s:
            if char in openCloseDict:
                charStack.append(char)
            
            else:
                if len(charStack) == 0:
                    return False
                
                openingChar = charStack.pop()

                if openCloseDict[openingChar] != char:
                    return False
        
        return len(charStack) == 0

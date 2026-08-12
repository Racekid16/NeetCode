class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for string in strs:
            stringLen = len(string)
            stringLenString = "0" * (3 - len(str(stringLen))) + str(stringLen)
            encodedString += stringLenString + string
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedList = []

        sIndex = 0

        while sIndex < len(s):
            stringLen = int(s[sIndex : sIndex + 3])
            decodedList.append(s[sIndex + 3 : sIndex + 3 + stringLen])

            sIndex = sIndex + 3 + stringLen
        
        return decodedList
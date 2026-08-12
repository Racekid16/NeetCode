class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = dict()

        for string in strs:
            stringSorted = "".join(sorted(string))

            if stringSorted not in anagramGroups:
                anagramGroups[stringSorted] = []

            anagramGroups[stringSorted].append(string)
        
        returnList = []

        for anagramGroupKey in anagramGroups:
            returnList.append(anagramGroups[anagramGroupKey])
        
        return returnList
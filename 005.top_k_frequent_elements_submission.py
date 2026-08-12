class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is number, value is frequency in nums
        numFrequencyDict = dict()

        for num in nums:
            numFrequencyDict[num] = numFrequencyDict.get(num, 0) + 1

        # a list where index i is a list of numbers
        # that appear i  + 1 times in nums.
        # a number can appear at most len(nums) times.
        frequencyNumList = [[] for _ in range(len(nums))]

        for numKey in numFrequencyDict:
            numFrequency = numFrequencyDict[numKey]
            frequencyNumList[numFrequency - 1].append(numKey)

        returnList = []
        frequencyIndex = len(frequencyNumList) - 1
        
        while frequencyIndex >= 0 and len(returnList) < k:
            for num in frequencyNumList[frequencyIndex]:
                returnList.append(num)
            
            frequencyIndex -= 1
        
        return returnList


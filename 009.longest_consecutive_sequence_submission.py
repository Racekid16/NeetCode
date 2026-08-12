class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequenceLen = 0

        numsSet = set(nums)

        for num in numsSet:
            if num - 1 not in numsSet:
                thisSequenceLen = 1
                numInSequence = num

                while numInSequence + 1 in numsSet:
                    thisSequenceLen += 1
                    numInSequence += 1
                
                if thisSequenceLen > longestSequenceLen:
                    longestSequenceLen = thisSequenceLen
        
        return longestSequenceLen
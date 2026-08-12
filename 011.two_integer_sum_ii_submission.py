class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers) - 1

        while leftPtr < rightPtr:
            leftNum = numbers[leftPtr]
            rightNum = numbers[rightPtr]
            numSum = leftNum + rightNum

            if numSum == target:
                return [leftPtr + 1, rightPtr + 1]
            
            if numSum < target:
                leftPtr += 1
            
            if numSum > target:
                rightPtr -= 1
        
        return [-1, -1]
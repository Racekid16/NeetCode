class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        solutions = []

        for numIndex in range(len(nums)):
            if numIndex > 0 and nums[numIndex] == nums[numIndex - 1]:
                continue

            leftPtr = numIndex + 1
            rightPtr = len(nums) - 1

            while leftPtr < rightPtr:
                numSum = nums[numIndex] + nums[leftPtr] + nums[rightPtr]

                if numSum == 0:
                    solutions.append([nums[numIndex], nums[leftPtr], nums[rightPtr]])
                    leftPtr += 1
                    rightPtr -= 1

                    while leftPtr < rightPtr and nums[leftPtr] == nums[leftPtr - 1]:
                        leftPtr += 1

                    while leftPtr < rightPtr and nums[rightPtr] == nums[rightPtr + 1]:
                        rightPtr -= 1

                elif numSum < 0:
                    leftPtr += 1
    
                else:
                    rightPtr -= 1

        return solutions

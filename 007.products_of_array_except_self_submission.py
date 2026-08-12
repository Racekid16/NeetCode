class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIndices = [index for index in range(len(nums)) if nums[index] == 0]

        if len(zeroIndices) > 1:
            return [0 for _ in range(len(nums))]
        
        if len(zeroIndices) == 1:
            product = 1
    
            for numIndex in range(len(nums)):
                if numIndex != zeroIndices[0]:
                    product *= nums[numIndex]
    
            return [0 if numIndex != zeroIndices[0] else product for numIndex in range(len(nums))]
        
        product = 1
    
        for num in nums:
            product *= num

        return [int(product / num) for num in nums]
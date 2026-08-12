class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def genPerms(curr, permLength):
            if permLength == len(nums):
                permutations.append(curr.copy())
                return
            
            for i in range(permLength, len(nums), 1):
                curr[permLength], curr[i] = curr[i], curr[permLength]
                genPerms(curr, permLength + 1)
                curr[permLength], curr[i] = curr[i], curr[permLength]
        
        genPerms(nums, 0)

        return permutations
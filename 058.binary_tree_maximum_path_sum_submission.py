# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # largest sum of any path found so far
        res = -float('inf')

        # return max sum of path ending at node
        # and update res
        def dfs(node):
            nonlocal res

            if node is None:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            
            returnVal = node.val
            if leftSum >= rightSum and leftSum > 0:
                returnVal += leftSum
            elif rightSum >= leftSum and rightSum > 0:
                returnVal += rightSum
            
            thisSum = node.val
            if leftSum > 0:
                thisSum += leftSum
            if rightSum > 0:
                thisSum += rightSum

            res = max(res, thisSum)
            return returnVal       
        
        dfs(root)
        return res
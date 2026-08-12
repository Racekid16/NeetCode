# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        # update res and return height of node
        def dfs(node):
            if node is None:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            nonlocal res
            res = max(res, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        # traverses tree, updates count along the way
        def dfs(node, maxSoFar):
            if node is None:
                return
            
            if maxSoFar <= node.val:
                nonlocal count
                count += 1
            
            newMax = max(node.val, maxSoFar)
            dfs(node.left, newMax)
            dfs(node.right, newMax)
        
        dfs(root, root.val)

        return count
        
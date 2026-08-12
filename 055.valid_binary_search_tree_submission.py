# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkNode(node, minVal, maxVal):
            if node is None:
                return True

            if node.val <= minVal or node.val >= maxVal:
                return False
            
            return checkNode(node.left, minVal, node.val) and checkNode(node.right, node.val, maxVal)
        
        return checkNode(root, -float('inf'), float('inf'))
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        step = 0
        returnVal = -1

        def inorder(node):
            nonlocal step, returnVal

            if node is None:
                return -1
            
            inorder(node.left)

            step += 1
            if step == k:
                returnVal = node.val
                return

            inorder(node.right)
        
        inorder(root)
        return returnVal
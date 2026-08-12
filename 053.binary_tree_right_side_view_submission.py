# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root is None:
            return []
        
        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            res.append(queue[-1].val)

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left is not None:
                    queue.append(node.left)
                
                if node.right is not None:
                    queue.append(node.right)
        
        return res
                

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root is None:
            return res
        
        # queue element takes form [node, levelOfNode]
        queue = deque()
        queue.append([root, 0])

        while len(queue) != 0:
            nodeInfo = queue.popleft()
            node = nodeInfo[0]
            nodeLevel = nodeInfo[1]

            if nodeLevel == len(res):
                res.append([])
            
            res[nodeLevel].append(node.val)

            if node.left is not None:
                queue.append([node.left, nodeLevel + 1])
            if node.right is not None:
                queue.append([node.right, nodeLevel + 1])
        
        return res
        
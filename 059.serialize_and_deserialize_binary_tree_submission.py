# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import json

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodeList = [None]

        stack = []
        # node, listIndex
        stack.append([root, 1])

        while len(stack) > 0:
            pair = stack.pop()
            node = pair[0]
            nodeIndex = pair[1]

            if node is None:
                continue

            while len(nodeList) <= nodeIndex:
                nodeList.append(None)
            nodeList[nodeIndex] = node.val

            stack.append([node.left, nodeIndex * 2])
            stack.append([node.right, nodeIndex * 2 + 1])

        return json.dumps(nodeList)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeList = json.loads(data)
        
        # return newly created node
        def dfs(index):
            nonlocal nodeList

            if index >= len(nodeList):
                return None

            nodeVal = nodeList[index]

            if nodeVal is None:
                return None
            
            node = TreeNode(nodeVal)
            node.left = dfs(index * 2)
            node.right = dfs(index * 2 + 1)

            return node
        
        return dfs(1)


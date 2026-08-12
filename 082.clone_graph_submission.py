"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # queue of original nodes
        q = deque()
        q.append(node)

        # map original nodes to new nodes
        originalToCopy = dict()
        originalToCopy[node] = Node(node.val)

        while len(q) > 0:
            cur = q.popleft()

            for neighbor in cur.neighbors:
                if neighbor not in originalToCopy:
                    originalToCopy[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                originalToCopy[cur].neighbors.append(originalToCopy[neighbor])

        return originalToCopy[node]
        
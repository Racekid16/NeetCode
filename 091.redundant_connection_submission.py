from scipy.cluster.hierarchy import DisjointSet

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = DisjointSet()
        n = len(edges)
        for node in range(1, n + 1):
            ds.add(node)

        for edge in edges:
            a = edge[0]
            b = edge[1]
            if ds.connected(a, b):
                return edge
            ds.merge(a, b)

from scipy.cluster.hierarchy import DisjointSet

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ds = DisjointSet()

        for node in range(n):
            ds.add(node)
        
        for edge in edges:
            a = edge[0]
            b = edge[1]
            if ds.connected(a, b):
                return False
            ds.merge(a, b)
        
        return ds.n_subsets == 1
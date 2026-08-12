from scipy.cluster.hierarchy import DisjointSet

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet()

        for node in range(n):
            ds.add(node)
        
        for edge in edges:
            a = edge[0]
            b = edge[1]
            ds.merge(a, b)
        
        return ds.n_subsets
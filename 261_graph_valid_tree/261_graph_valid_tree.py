class Solution:
    def validTree(self, n, edges):
        parent = list(range(n))

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        for edge in edges:
            u, v = edge
            root_u = find(u)
            root_v = find(v)
        if root_u == root_v:
            return False
        parent[root_u] = root_v
    return len(set(find(i) for i in range(n))) == 1
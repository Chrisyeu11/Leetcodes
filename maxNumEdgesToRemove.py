#https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/submissions/1304282388/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.count = size  # Count of connected components
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            self.count -= 1
            return True
        return False
    
    def connected(self):
        # Check if all nodes are connected (single connected component)
        return self.count == 2  # Since we have nodes from 1 to n, count should be n + 1 initially

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)
        
        edges_used = 0
        
        # Step 1: Add type 3 edges (both Alice and Bob)
        for edge_type, u, v in edges:
            if edge_type == 3:
                if uf_alice.union(u, v) | uf_bob.union(u, v):
                    edges_used += 1
        
        # Step 2: Add type 1 edges (only Alice)
        for edge_type, u, v in edges:
            if edge_type == 1 and uf_alice.union(u, v):
                edges_used += 1
        
        # Step 3: Add type 2 edges (only Bob)
        for edge_type, u, v in edges:
            if edge_type == 2 and uf_bob.union(u, v):
                edges_used += 1
        
        # Step 4: Check if both Alice and Bob can traverse the entire graph
        if uf_alice.connected() and uf_bob.connected():
            return len(edges) - edges_used
        else:
            return -1

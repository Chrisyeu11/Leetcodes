#https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/submissions/1303423784/
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Create adjacency list for the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)
        
        # Step 2: Function to perform DFS and collect ancestors
        def dfs(node: int, visited: List[bool], ancestors: Set[int]) -> Set[int]:
            if visited[node]:
                return ancestors[node]
            visited[node] = True
            for parent in graph[node]:
                ancestors[node].update(dfs(parent, visited, ancestors))
                ancestors[node].add(parent)
            return ancestors[node]

        # Step 3: Initialize data structures
        visited = [False] * n
        ancestors = [set() for _ in range(n)]
        
        # Step 4: Perform DFS for each node
        for i in range(n):
            if not visited[i]:
                dfs(i, visited, ancestors)
        
        # Step 5: Convert sets to sorted lists
        return [sorted(list(ancestors[i])) for i in range(n)]

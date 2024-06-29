#https://leetcode.com/problems/maximum-total-importance-of-roads/description/?envType=daily-question&envId=2024-06-28+
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Create a list to count the number of connections for each city
        connections = [0] * n
        
        # Step 2: Count the number of roads connected to each city
        for road in roads:
            connections[road[0]] += 1
            connections[road[1]] += 1
        
        # Step 3: Sort the connections in descending order
        connections.sort(reverse=True)
        
        # Step 4: Assign importances and calculate the total importance
        total_importance = sum(connections[i] * (n - i) for i in range(n))
        
        return total_importance

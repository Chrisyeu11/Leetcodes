#https://leetcode.com/problems/find-center-of-star-graph/description/?envType=daily-question&envId=2024-06-27
class Solution:
    # Defines a class named Solution
    def findCenter(self, edges: List[List[int]]) -> int:
        # Defines a method findCenter that takes a parameter edge, which is a list of lists of integers, and returns an integer

        # Check the first two edges
        # Checks if the first element of the first edge is equal to the first or second element of the second edge
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
            # If the first element of the first edge matches either element of the second edge, it is the center of the star graph

        else:
            return edges[0][1]
            # Otherwise, the second element of the first edge must be the center of the star graph

#https://leetcode.com/problems/find-the-winner-of-the-circular-game/submissions/1313396755/?envType=daily-question&envId=2024-07-08
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Create a list of friends numbered from 1 to n
        friends = list(range(1, n+1))
        
        # Start at the first position
        current = 0
        
        # Continue until only one friend remains
        while len(friends) > 1:
            # Calculate the position of the friend to remove
            # We subtract 1 because we're counting k steps starting from the current position
            # The modulo operation wraps around the list if we reach the end
            current = (current + k - 1) % len(friends)
            
            # Remove the friend at the calculated position
            friends.pop(current)
            
            # Note: We don't need to update 'current' here because after removing a friend,
            # The next friend automatically takes this position
        
        # Return the last remaining friend
        return friends[0]

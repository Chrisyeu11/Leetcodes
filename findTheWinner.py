#https://leetcode.com/problems/find-the-winner-of-the-circular-game/submissions/1313396755/?envType=daily-question&envId=2024-07-08
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        current = 0
        
        while len(friends) > 1:
            current = (current + k - 1) % len(friends)
            friends.pop(current)
            
        return friends[0]

#https://leetcode.com/problems/pass-the-pillow/?envType=daily-question&envId=2024-07-06
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Calculate the effective position of the pillow in a single pass back and forth
        cycle_length = n * 2 - 2
        position_in_cycle = time % cycle_length
        
        # Determine the exact position based on the position in the cycle
        if position_in_cycle < n:
            return position_in_cycle + 1
        else:
            return n * 2 - position_in_cycle - 1

#https://leetcode.com/problems/three-consecutive-odds/
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] & 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False

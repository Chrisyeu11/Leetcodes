#https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/?envType=daily-question&envId=2024-07-03
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If the list has 4 or fewer elements, we can make all elements equal
        # by changing up to 3 elements, so the minimum difference is 0
        if len(nums) <= 4:
            return 0
        
        # Sort the list in ascending order
        nums.sort()
        
        # Initialize the answer with the difference between the largest and smallest elements
        ans = nums[-1] - nums[0]
        
        # Check four possible scenarios:
        # 1. Change the 3 smallest elements
        # 2. Change the 2 smallest and 1 largest elements
        # 3. Change the 1 smallest and 2 largest elements
        # 4. Change the 3 largest elements
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        
        return ans

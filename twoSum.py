#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Create a dictionary to store the number and its index
        num_to_index = {}
        
        # Step 2: Iterate through the list of numbers with their indices
        for index, num in enumerate(nums):
            # Step 3: Calculate the complement of the current number
            complement = target - num
            
            # Step 4: Check if the complement exists in the dictionary
            if complement in num_to_index:
                # Step 5: If it exists, return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # Step 6: If the complement does not exist, add the current number and its index to the dictionary
            num_to_index[num] = index
        
        # Step 7: Return an empty list if no solution is found (though the problem guarantees one solution)
        return []

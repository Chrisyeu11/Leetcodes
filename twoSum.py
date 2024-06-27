class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the number and its index
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # If it exists, return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # If the complement does not exist, add the current number and its index to the dictionary
            num_to_index[num] = index
        
        # Return an empty list if no solution is found (though the problem guarantees one solution)
        return []

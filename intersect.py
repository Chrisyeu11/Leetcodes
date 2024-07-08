#https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/1306460651/?envType=daily-question&envId=2024-07-02
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a Counter object to count occurrences of each number in nums1
        counts = Counter(nums1)
        
        # Initialize an empty list to store the intersection
        intersection = []
        
        # Iterate through each number in nums2
        for num in nums2:
            # If the number exists in counts and has a positive count
            if counts[num] > 0:
                # Add the number to the intersection list
                intersection.append(num)
                # Decrease the count for this number
                counts[num] -= 1
        
        # Return the list of intersecting elements
        return intersection

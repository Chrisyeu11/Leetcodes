#https://leetcode.com/problems/concatenation-of-array/
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
#or 
#class Solution:
#    def getConcatenation(self, nums: List[int]) -> List[int]:
#        return nums + nums

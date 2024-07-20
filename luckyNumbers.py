#https://leetcode.com/problems/lucky-numbers-in-a-matrix/?envType=daily-question&envId=2024-07-20
from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_row = {min(row) for row in matrix}
        max_col = {max(col) for col in zip(*matrix)}
        return list(min_row & max_col)

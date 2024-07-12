#https://leetcode.com/problems/maximum-score-from-removing-substrings/submissions/1318143978/?envType=daily-question&envId=2024-07-12
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def calculate_points(s: str, first: str, second: str, points: int) -> (str, int):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score
        
        if x >= y:
            s, score = calculate_points(s, 'a', 'b', x)
            _, additional_score = calculate_points(s, 'b', 'a', y)
        else:
            s, score = calculate_points(s, 'b', 'a', y)
            _, additional_score = calculate_points(s, 'a', 'b', x)
        
        return score + additional_score

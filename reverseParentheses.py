#https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/?envType=daily-question&envId=2024-07-11
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                queue = []
                while stack[-1] != '(':
                    queue.append(stack.pop())
                stack.pop()  # remove the '('
                stack.extend(queue)
            else:
                stack.append(char)
        return ''.join(stack)

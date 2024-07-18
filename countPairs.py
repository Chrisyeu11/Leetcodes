#https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/submissions/1324720779/?envType=daily-question&envId=2024-07-18
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.ans += 1
            return [n + 1 for n in left + right if n + 1 < distance]
        
        dfs(root)
        return self.ans

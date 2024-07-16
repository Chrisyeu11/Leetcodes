https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/submissions/1322426157/?envType=daily-question&envId=2024-07-16

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Helper function to find the path from the root to a given target node
        def find_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            if node.left and find_path(node.left, target, path):
                path.append('L')
                return True
            if node.right and find_path(node.right, target, path):
                path.append('R')
                return True
            return False
        
        # Find paths from root to start and destination nodes
        start_path = []
        dest_path = []
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)
        
        # Reverse paths to get the correct order from root to nodes
        start_path = start_path[::-1]
        dest_path = dest_path[::-1]
        
        # Find common prefix length
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1
        
        # Calculate the steps to go from start to destination
        # Steps to go up from start to the common ancestor
        up_steps = 'U' * (len(start_path) - i)
        # Steps to go down from the common ancestor to the destination
        down_steps = ''.join(dest_path[i:])
        
        return up_steps + down_steps

# Test case
sol = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

startValue = 3
destValue = 6
print(sol.getDirections(root, startValue, destValue))  # Output: "UURL"

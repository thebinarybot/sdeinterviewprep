# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0 
        
        def maxDepth(root):
            if root is None:
                return 0

            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            
            self.dia = max(self.dia, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        maxDepth(root)  
        return self.dia

# Question: https://leetcode.com/problems/diameter-of-binary-tree/
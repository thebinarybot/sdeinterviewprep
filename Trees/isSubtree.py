# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.isSameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None or root1.val != root2.val:
            return False
        
        return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)

# Question: https://leetcode.com/problems/subtree-of-another-tree/

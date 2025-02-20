# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        tree1 = []
        tree2 = []
        
        def preOrder(root, tree):
            if root is None:
                tree.append("null")
                return 
            tree.append(root.val)
            preOrder(root.left, tree)
            preOrder(root.right, tree)
        
        preOrder(p, tree1)
        preOrder(q, tree2)
        return tree1 == tree2

# Question: https://leetcode.com/problems/same-tree/
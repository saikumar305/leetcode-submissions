# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            a=b=0

            if node.left:
                if not node.left.left and not node.left.right:
                    a=node.left.val
                else:
                    a=helper(node.left)
            if node.right:
                b= helper(node.right)
            
            return a+b

        return helper(root)
        
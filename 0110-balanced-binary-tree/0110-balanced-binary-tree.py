# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return abs(left-right) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def maxDepth(self,root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        
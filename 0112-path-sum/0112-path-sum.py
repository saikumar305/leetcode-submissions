# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        if not root.left and not root.right and root.val == target: return True
        return self.hasPathSum(root.left, target-root.val) or self.hasPathSum(root.right, target-root.val)

        
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
        def helper(node):
            if not node:
                return (0, True)

            left_height, left_balanced = helper(node.left)
            right_height, right_balanced = helper(node.right)

            current_balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )

            current_height = max(left_height, right_height) + 1

            return (current_height, current_balanced)

        _, is_balanced = helper(root)
        return is_balanced
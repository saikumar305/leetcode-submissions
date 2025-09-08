# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float('inf')
        if not root:
            return 0
        def inorder(node):
            if not node: return
            inorder(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val-self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)

        return self.ans
        

        
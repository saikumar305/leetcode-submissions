# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def swap(root , left, right):

    root.left = right
    root.right = left
    return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root = swap(root, left, right)

        return root        

        
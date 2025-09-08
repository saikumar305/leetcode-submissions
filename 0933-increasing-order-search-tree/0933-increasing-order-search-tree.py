# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        ans = []

        def inorder(node):
            if not node:
                return
            
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        inorder(root)

        # ans.sort()
    

        tree = TreeNode(val = ans[0])

        head = tree

        for i in ans[1:]:
            head.right = TreeNode(i)
            head = head.right
        return tree


        
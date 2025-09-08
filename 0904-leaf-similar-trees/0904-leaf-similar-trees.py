# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_vals(node , leaf_nodes):
            if not node: return
            if not node.left and not node.right:
                leaf_nodes.append(node.val)
            get_leaf_vals(node.left, leaf_nodes)
            get_leaf_vals(node.right, leaf_nodes)
            
        
        leaf_vals1 = []
        leaf_vals2 = []

        get_leaf_vals(root1, leaf_vals1)
        get_leaf_vals(root2, leaf_vals2)

        print(leaf_vals1 , leaf_vals2)
        return leaf_vals1 == leaf_vals2
        
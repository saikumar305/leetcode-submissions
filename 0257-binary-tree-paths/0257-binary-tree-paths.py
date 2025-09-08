# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if not root.left and not root.right:
        #     return [str(root.val)]
        # ans = []

        # left = []
        # right = []

        # def inorder(node, vals):
        #     if not node:
        #         return

        #     vals.append(str(node.val))
        #     if root.left:
        #         inorder(node.left,vals)
        #     if root.right:
        #         inorder(node.right, vals)

        # inorder(root.left , left)
        # inorder(root.right, right)

        

        # if left:
        #     left = str(root.val) + "->" + "->".join(left)
        # if right:
        #     right = str(root.val) + "->" + "->".join(right)
        


        # if left and right:
        #     return [left, right]
        # if left and not right:
        #     return [left]
        # else:
        #     return [right]

        op = []
        path = []
        self.dfs(root, path, op)

        return op



    def dfs(self, root, path, output):
        path.append(str(root.val))

        if not root.left and  not root.right:
            output.append('->'.join(path))
            path.pop()
            return 

        if root.left:  self.dfs(root.left , path , output)
        if root.right: self.dfs(root.right, path, output)

        path.pop()

    

        
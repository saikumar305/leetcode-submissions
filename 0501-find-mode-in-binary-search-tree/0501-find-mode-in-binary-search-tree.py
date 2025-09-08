# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}

        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            count[node.val] = count.get(node.val , 0) + 1
            
            inorder(node.right)
        
        inorder(root)

        maxx = max(count.values())
        res= []
        for i in count.keys():
            if count[i] == maxx:
                res.append(i)
        

        return  res

        
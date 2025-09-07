"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:return []

        q = [root]
        op = []

        while any(q):
            op.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]

        return op

        
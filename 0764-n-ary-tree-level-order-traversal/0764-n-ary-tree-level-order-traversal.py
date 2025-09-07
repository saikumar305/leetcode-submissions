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

        op = []

        q = deque([root])

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()

                level += [node.val]

                for n in node.children: q.append(n)

            op += [level]

        return op

        
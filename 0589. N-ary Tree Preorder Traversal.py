"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        def traversal(node):
            if node:
                res.append(node.val)
                for new in node.children:
                    traversal(new)
        traversal(root)
        return res
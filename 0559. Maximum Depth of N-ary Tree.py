"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res=[0]
        if not root:
            return 0
        def teverse(node,n):
            res[0]=max(res[0],n)
            for c in node.children:
                teverse(c,n+1)
        teverse(root,1)
        return res[0]

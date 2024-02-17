"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q=[root]
        res=[]
        while q:
            cur=[]
            new=[]
            for node in q:
                cur.append(node.val)
                for i in node.children:
                    new.append(i)
            q=new
            res.append(cur)
        return res
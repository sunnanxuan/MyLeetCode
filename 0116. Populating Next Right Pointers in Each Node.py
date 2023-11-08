"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        dummy=cur=pre=Node(0)
        q=[root]
        while q:
            new=[]
            for c in q:
                cur.next=c
                cur=cur.next
                if c.left:
                    new.append(c.left)
                if c.right:
                    new.append(c.right)
                c.left=None
                c.right=None
                cur.next=c
                cur=cur.next
            pre=cur
            cur.next=Node('#')
            cur=cur.next
            q=new
        pre.next=None
        return dummy.next
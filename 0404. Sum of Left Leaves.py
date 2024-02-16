# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left=[root]
        right=[]
        res=0
        while left or right:
            nl=[]
            nr=[]
            for l in left:
                if not l.left and not l.right and l!=root:
                    res+=l.val
                else:
                    if l.left:
                        nl.append(l.left)
                    if l.right:
                        nr.append(l.right)
            for r in right:
                if r.left:
                    nl.append(r.left)
                if r.right:
                    nr.append(r.right)
            left=nl
            right=nr
        return res
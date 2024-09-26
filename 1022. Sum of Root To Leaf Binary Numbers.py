# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res=0
        q=[(root,str(root.val))]
        while q:
            new=[]
            for n,c in q:
                if not n.left and not n.right:
                    res+=int(c,2)
                if n.left:
                    new.append((n.left,c+str(n.left.val)))
                if n.right:
                    new.append((n.right,c+str(n.right.val)))
            q=new
        return res

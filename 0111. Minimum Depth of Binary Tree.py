# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[root]
        n=0
        while q:
            new=[]
            for c in q:
                if not c.left and not c.right:
                    return n+1
                if c.left:
                    new.append(c.left)
                if c.right:
                    new.append(c.right)
            q=new
            n+=1
        return n
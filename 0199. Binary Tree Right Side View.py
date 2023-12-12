# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[root.val]
        q=[root]
        while q:
            new=[]
            for node in q:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            q=new
            if new:
                n=new[-1]
                res.append(n.val)
        return res

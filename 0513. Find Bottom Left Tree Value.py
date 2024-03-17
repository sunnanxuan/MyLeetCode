# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=[root]
        while q:
            new=[]
            for node in q:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            if not new:
                return q[0].val
            else:
                q=new
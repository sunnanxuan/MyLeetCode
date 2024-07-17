# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findleaf(node):
            if not node.left and not node.right:
                return [node.val]
            l=[]
            r=[]
            if node.left:l=findleaf(node.left)
            if node.right:r=findleaf(node.right)
            return l+r
        leaf1=findleaf(root1)
        leaf2=findleaf(root2)
        return leaf1==leaf2
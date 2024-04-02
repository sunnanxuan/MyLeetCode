# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res=[0]
        def tilt(node):
            if not node:
                return 0
            else:
                l=tilt(node.left)
                r=tilt(node.right)
                res[0]+=abs(l-r)
                return node.val+l+r
        tilt(root)
        return res[0]
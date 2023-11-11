# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[float('-inf')]
        def maxsum(node):
            if not node:
                return 0
            else:
                node.val=max(node.val,node.val+max(maxsum(node.left),maxsum(node.right)))
                if not node.left or not node.right:
                    sm=node.val
                else:
                    sm=max(node.val,node.val+min(node.left.val,node.right.val))
                res[0]=max(res[0],sm)

                return node.val
        maxsum(root)

        return res[0]
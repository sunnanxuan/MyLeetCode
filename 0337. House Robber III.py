# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def travel(node):
            if not node:
                return [0, 0]
            else:
                l = travel(node.left)
                r = travel(node.right)
                return [node.val + l[1] + r[1], max(l) + max(r)]

        return max(travel(root))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def traverse(node, mn, mx):
            if not node:
                return
            else:
                self.res = max(self.res, abs(mn - node.val), abs(mx - node.val))
                traverse(node.left, min(mn, node.val), max(mx, node.val))
                traverse(node.right, min(mn, node.val), max(mx, node.val))

        traverse(root.left, root.val, root.val)
        traverse(root.right, root.val, root.val)
        return self.res


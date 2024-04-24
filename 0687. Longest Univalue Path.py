# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def find(node):
            if not node:
                m = n = 0
            else:
                l = find(node.left)
                r = find(node.right)
                if (node.left and node.left.val == node.val) and (node.right and node.right.val == node.val):
                    n = l + r + 1
                    m = max(l + 1, r + 1)

                elif node.left and node.left.val == node.val:
                    m = n = l + 1

                elif node.right and node.right.val == node.val:
                    m = n = r + 1
                else:
                    m = n = 1
            res[0] = max(res[0], n)
            return m

        if not root: return 0
        find(root)
        return res[0] - 1
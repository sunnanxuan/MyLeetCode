# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [0]

        def traverse(node):
            if node:
                if low <= node.val <= high: res[0] += node.val
                if node.val >= low:
                    traverse(node.left)
                if node.val <= high:
                    traverse(node.right)

        traverse(root)
        return res[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def traverse(node):
            if node:
                values.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        values.sort()
        return min([values[i] - values[i - 1] for i in range(1, len(values))])

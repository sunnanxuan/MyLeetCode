# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(node, pre):
            if node.right:
                node.val += traverse(node.right, pre)
            else:
                node.val += pre
            if node.left:
                return traverse(node.left, node.val)
            else:
                return node.val

        traverse(root, 0)
        return root


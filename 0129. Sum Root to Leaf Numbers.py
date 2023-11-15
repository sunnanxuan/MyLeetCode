# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sm = [0]

        def traverse(node, s):
            if not node.left and not node.right:
                sm[0] += int(s)
            if node.left:
                traverse(node.left, s + str(node.left.val))
            if node.right:
                traverse(node.right, s + str(node.right.val))

        traverse(root, str(root.val))
        return sm[0]
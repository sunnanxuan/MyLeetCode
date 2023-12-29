# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
      values=[]
      def traverse(node):
        if node.left:
          traverse(node.left)
        values.append(node.val)
        if node.right:
          traverse(node.right)
      traverse(root)
      return values[k-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traverse(node):
            l=r=''
            if node.left:
                l=traverse(node.left)
            if node.right:
                r=traverse(node.right)

            if not l and not r:
                return '{}'.format(str(node.val))
            elif not l:
                return '{}()({})'.format(str(node.val),r)
            elif not r:
                return '{}({})'.format(str(node.val),l)
            else:
                return '{}({})({})'.format(str(node.val),l,r)
        res=traverse(root)
        return res
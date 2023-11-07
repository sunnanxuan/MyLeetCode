# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dummy=cur=TreeNode(0)
        def traverse(node,cur):
            cur.right=node
            cur=cur.right
            l=node.left
            r=node.right
            node.left=None
            node.right=None
            if l:
                cur=traverse(l,cur)
            if r:
                cur=traverse(r,cur)
            return cur
        if not root:
            return root
        traverse(root,cur)
        root=dummy.right

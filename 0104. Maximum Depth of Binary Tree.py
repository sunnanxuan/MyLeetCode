# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        md=[0]
        def traverse(node,n):
            if node:
                n+=1
                md[0]=max(md[0],n)
                if node.left:
                    traverse(node.left,n)
                if node.right:
                    traverse(node.right,n)
        traverse(root,0)
        return md[0]
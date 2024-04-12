# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy=TreeNode(val)
        dummy.left=root
        def traverse(node,n,pre,p):
            if n==depth:
                add=TreeNode(val)
                if p=='L':
                    pre.left=add
                    add.left=node
                elif p=='R':
                    pre.right=add
                    add.right=node
            elif n<depth and node:
                traverse(node.left,n+1,node,'L')
                traverse(node.right,n+1,node,'R')
        traverse(root,1,dummy,'L')
        return dummy.left

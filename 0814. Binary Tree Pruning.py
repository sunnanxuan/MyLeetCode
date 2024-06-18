# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(node):
            if node:
                l=prune(node.left)
                r=prune(node.right)
                if not l:
                    node.left=None
                if not r:
                    node.right=None
                if node.val or l or r:
                    return True
                else:return False
            return False
        res=prune(root)
        if not res:return None
        else:return root
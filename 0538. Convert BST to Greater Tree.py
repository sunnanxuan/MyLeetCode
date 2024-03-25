# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def convert(node,pre):
            if not node:
                return 0
            else:
                if not node.right:
                    node.val=node.val+convert(node.right,pre)+pre
                else:
                    node.val=node.val+convert(node.right,pre)
                l=convert(node.left,node.val)
                return l and l or node.val
        convert(root,0)
        return root

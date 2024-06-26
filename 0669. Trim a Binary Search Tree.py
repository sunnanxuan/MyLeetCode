# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            if not node:
                return None
            if node.val<low:
                return trim(node.right)
            elif node.val>high:
                return trim(node.left)
            else:
                node.right=trim(node.right)
                node.left=trim(node.left)
                return node
        return trim(root)

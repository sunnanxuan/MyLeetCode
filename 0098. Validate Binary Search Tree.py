# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(l, r, node):
            if not node:
                return True
            else:
                bl = br = True
                if node.val <= l or node.val >= r:
                    return False
                return traverse(max(l, node.val), r, node.right) and traverse(l, min(r, node.val), node.left)

        return traverse(-float('inf'), float('inf'), root)

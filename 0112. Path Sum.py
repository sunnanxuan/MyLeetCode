# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def add(sm, node):
            if not node.left and not node.right:
                if sm + node.val == targetSum:
                    return True
                else:
                    return False
            elif node.left and node.right:
                return add(sm + node.val, node.left) or add(sm + node.val, node.right)
            elif node.left:
                return add(sm + node.val, node.left)
            elif node.right:
                return add(sm + node.val, node.right)

        if not root:
            return False
        return add(0, root)
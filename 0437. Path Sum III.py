# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        res = [0]

        def path(node, pre):
            new = []
            if node.val == targetSum:
                res[0] += 1
            new.append(node.val)
            for m in pre:
                if node.val + m == targetSum:
                    res[0] += 1
                new.append(node.val + m)
            if node.left:
                path(node.left, new)
            if node.right:
                path(node.right, new)

        if not root:
            return 0
        path(root, [])
        return res[0]

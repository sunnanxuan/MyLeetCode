# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values=set()
        def traverse(root):
            if root:
                if k-root.val in values:
                    return True
                else:
                    values.add(root.val)
                    return traverse(root.left) or traverse(root.right)
            else:return False
        return traverse(root)
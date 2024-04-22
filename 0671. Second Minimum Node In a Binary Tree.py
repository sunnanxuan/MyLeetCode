# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values=set()
        def traverse(node):
            if node:
                values.add(node.val)
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        lst=sorted(list(values))
        if len(lst)==1:return -1
        else:return lst[1]
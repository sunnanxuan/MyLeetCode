# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values=[]
        def traverse(node):
            if node:
                values.append(node.val)
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        values.sort()
        diff=[values[i+1]-values[i] for i in range(len(values)-1)]
        return min(diff)
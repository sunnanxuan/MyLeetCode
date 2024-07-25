# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = []

        def traverse(node):
            vals.append(node.val)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)
        vals.sort(reverse=True)
        v = vals.pop()
        head = cur = TreeNode(v)
        while vals:
            cur.right = TreeNode(vals.pop())
            cur = cur.right
        return head

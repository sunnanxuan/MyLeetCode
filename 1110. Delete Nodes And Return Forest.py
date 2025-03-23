# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        res = []

        def traverse(node, pre, p):
            if not node:
                return
            elif node.val in to_delete:
                if pre:
                    if p == 'L':
                        pre.left = None
                    else:
                        pre.right = None
                traverse(node.left, None, '')
                traverse(node.right, None, '')
            else:
                if not pre:
                    res.append(node)
                traverse(node.left, node, 'L')
                traverse(node.right, node, 'R')

        traverse(root, None, '')
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find(node, pre, p):
            if not node:
                return [False, None, None, None]
            elif key == node.val:
                return [True, node, pre, p]
            elif key > node.val:
                return find(node.right, node, 'right')
            elif key < node.val:
                return find(node.left, node, 'left')

        result = find(root, None, None)
        if not result[0]:
            return root
        else:
            node = cur = result[1]
            pre = result[2]
            p = result[3]
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                l = node.left
                node = cur = node.right
                while cur.left:
                    cur = cur.left
                cur.left = l
            if not pre:
                root = node
            else:
                if p == 'left':
                    pre.left = node
                else:
                    pre.right = node
            return root


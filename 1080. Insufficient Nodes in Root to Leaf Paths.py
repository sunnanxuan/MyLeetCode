# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def traverse(node, t):
            if not node.left and not node.right:
                if node.val >= t:
                    return True
                else:
                    return False
            elif node.left and node.right:
                l = traverse(node.left, t - node.val)
                r = traverse(node.right, t - node.val)
                if not l: node.left = None
                if not r: node.right = None
                if l or r:
                    return True
                else:
                    return False
            elif node.left:
                l = traverse(node.left, t - node.val)
                if not l:
                    node.left = None
                    return False
                else:
                    return True
            elif node.right:
                r = traverse(node.right, t - node.val)
                if not r:
                    node.right = None
                    return False
                else:
                    return True

        head = TreeNode(0)
        head.left = root
        traverse(head, limit)
        return head.left




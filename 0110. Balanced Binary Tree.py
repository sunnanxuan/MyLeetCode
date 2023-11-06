# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def count(node):
            if not node:
                return 0
            else:
                node.val=1+max(count(node.left),count(node.right))
                return node.val
        count(root)
        def balance(node):
            if not node:
                return True
            else:
                if node.left and node.right:
                    if abs(node.left.val-node.right.val)>1:
                        return False
                    else:
                        return balance(node.left) and balance(node.right)
                elif (node.left and node.left.val>1) or (node.right and node.right.val>1):
                    return False
                else:
                    return True
        return balance(root)
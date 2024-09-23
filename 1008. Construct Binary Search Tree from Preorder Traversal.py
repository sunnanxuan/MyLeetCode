# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def construct(l, r):
            if l > r:
                return None
            else:
                cur = preorder[l]
                root = TreeNode(cur)
                i = l + 1
                while i <= r and preorder[i] < cur:
                    i += 1
                root.left = construct(l + 1, i - 1)
                root.right = construct(i, r)
                return root

        res = construct(0, len(preorder) - 1)
        return res
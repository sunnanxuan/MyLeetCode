# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        else:
            node = TreeNode(preorder.pop(0))
            postorder.pop()
            if preorder:
                l = preorder[0]
                r = postorder[-1]
                if l == r:
                    node.left = self.constructFromPrePost(preorder, postorder)
                else:
                    pl = postorder.index(l)
                    pr = preorder.index(r)
                    node.left = self.constructFromPrePost(preorder[:pr], postorder[:pl + 1])
                    node.right = self.constructFromPrePost(preorder[pr:], postorder[pl + 1:])

            return node

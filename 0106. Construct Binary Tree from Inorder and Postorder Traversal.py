# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            p=inorder.index(postorder.pop())
            root=TreeNode(inorder[p])
            if p<len(inorder)-1:
                root.right=self.buildTree(inorder[p+1:],postorder)
            if p>0:
                root.left=self.buildTree(inorder[:p],postorder)
        else:
            root=None
        return root
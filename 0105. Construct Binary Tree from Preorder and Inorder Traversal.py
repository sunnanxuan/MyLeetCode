class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            node = None
        else:
            n = preorder.pop(0)
            node = TreeNode(n)
            p = inorder.index(n)
            inl = inorder[:p]
            inr = inorder[p + 1:]
            node.left = self.buildTree(preorder, inl)
            node.right = self.buildTree(preorder, inr)
        return node


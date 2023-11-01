# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        arr = []
        dic = {}

        def inorder(node):
            if node.left:
                inorder(node.left)
            arr.append(node.val)
            dic[node.val] = node
            if node.right:
                inorder(node.right)

        inorder(root)
        lst = sorted(arr)
        p = []
        for i in range(len(lst)):
            if lst[i] != arr[i]:
                p.append(i)
        n1 = dic[arr[p[0]]]
        n2 = dic[arr[p[1]]]
        n1.val, n2.val = n2.val, n1.val

        return root
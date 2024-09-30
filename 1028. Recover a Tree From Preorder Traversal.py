# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        while i < len(traversal) and traversal[i] != '-':
            i += 1
        root = TreeNode(int(traversal[:i]))
        stack = [root]
        d = 0
        while i < len(traversal):
            j = i
            while j < len(traversal) and traversal[j] == '-':
                j += 1
            k = j
            while k < len(traversal) and traversal[k] != '-':
                k += 1
            while d > j - i:
                stack.pop()
                d -= 1
            if j - i == d:
                stack.pop()
                n = stack[-1]
                n.right = TreeNode(int(traversal[j:k]))
                stack.append(n.right)
            else:
                d += 1
                n = stack[-1]
                n.left = TreeNode(int(traversal[j:k]))
                stack.append(n.left)

            i = k
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        q = [['', root]]
        while q:
            new = []
            while q:
                p = q.pop()
                node = p.pop()
                p[0] += '->' + str(node.val)
                if not node.left and not node.right:
                    res.append(p[0][2:])

                else:
                    if node.left:
                        new.append(p + [node.left])
                    if node.right:
                        new.append(p + [node.right])
            q = new
        return res
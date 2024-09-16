# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def traverse(node):
            if not node:
                return []
            else:
                lst = traverse(node.left) + traverse(node.right)
                res = []
                if not lst:
                    res.append(chr(97 + node.val))
                else:
                    for c in lst:
                        res.append(c + chr(97 + node.val))
                return res

        arr = traverse(root)
        arr.sort()
        return arr[0]


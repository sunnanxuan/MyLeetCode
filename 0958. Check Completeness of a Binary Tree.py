# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        find = False
        while q:
            new = []
            for node in q:

                if node.left:
                    if not find:
                        new.append(node.left)
                    else:
                        return False
                else:
                    find = True
                if node.right:
                    if not find:
                        new.append(node.right)
                    else:
                        return False
                else:
                    find = True
            q = new
        return True

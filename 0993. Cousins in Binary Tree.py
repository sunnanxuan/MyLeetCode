# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        while q:
            new = []
            values = {}
            for node in q:
                if node.left:
                    new.append(node.left)
                    values[node.left.val] = node.val
                if node.right:
                    new.append(node.right)
                    values[node.right.val] = node.val
            q = new
            if x not in values and y not in values:
                continue
            elif x in values and y in values and values[x] != values[y]:
                return True
            else:
                return False

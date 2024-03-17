# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        res = []
        while q:
            new = []
            ma = float('-inf')
            for node in q:
                ma = max(ma, node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            q = new
            res.append(ma)
        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dic = {}
        p = set()
        q = [root]
        n = 1
        while any(q):
            new_q = []
            new_p = set()
            for node in q:
                if not node:
                    new_q.append(None)
                    new_q.append(None)
                else:
                    dic[n] = node
                    new_p.add(n)
                    new_q.append(node.left)
                    new_q.append(node.right)
                n += 1
            pre = new_p
            q = new_q

        while len(pre) > 1:
            new = set()
            for c in pre:
                new.add(c // 2)
            pre = new
        return dic[list(pre)[0]]






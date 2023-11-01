# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = sum([root.left == None, root.right == None])
        if not root or p == 2:
            return True
        elif sum([root.left == None, root.right == None]) == 1 or root.left.val != root.right.val:
            return False
        l = [root.left]
        r = [root.right]
        while l:
            nl = []
            nr = []
            for i in range(len(l)):
                p1 = sum([l[i].left == None, r[i].right == None])
                p2 = sum([l[i].right == None, r[i].left == None])
                if p1 == 1 or (p1 == 0 and l[i].left.val != r[i].right.val):
                    return False
                elif p1 == 0:
                    nl.append(l[i].left)
                    nr.append(r[i].right)
                if p2 == 1 or (p2 == 0 and l[i].right.val != r[i].left.val):
                    return False
                elif p2 == 0:
                    nl.append(l[i].right)
                    nr.append(r[i].left)
            l = nl
            r = nr
        return True

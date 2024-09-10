# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        q = [(root, 0)]
        while q:
            new = []
            cur = collections.defaultdict(list)
            for node, i in q:
                cur[i].append(node.val)
                if node.left:
                    new.append((node.left, i - 1))
                if node.right:
                    new.append((node.right, i + 1))
            q = new
            for k in cur:
                dic[k].extend(sorted(cur[k]))
        res = []
        for i in sorted(list(dic.keys())):
            res.append(dic[i])
        return res


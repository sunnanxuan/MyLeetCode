# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dic=collections.defaultdict(int)
        def sum(node):
            sm=node.val
            if node.left:
                sm+=sum(node.left)
            if node.right:
                sm+=sum(node.right)
            dic[sm]+=1
            return sm
        sum(root)
        m=max(dic.values())
        res=[k for k in dic if dic[k]==m]
        return res
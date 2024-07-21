# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2==0:return []
        memo={}
        def build(n):
            if n in memo:return memo[n]
            if n==1:return [TreeNode(0)]
            res=[]
            n-=1
            for l in range(1,n,2):
                r=n-l
                L=build(l)
                R=build(r)
                for ln in L:
                    for rn in R:
                        node=TreeNode(0)
                        node.left=ln
                        node.right=rn
                        res.append(node)
            memo[n]=res
            return res
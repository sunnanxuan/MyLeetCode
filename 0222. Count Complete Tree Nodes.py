# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[root]
        l=0
        res=0
        while q:
            if q[-1]:
                res+=(2**l)
                l+=1
                new=[]
                for cur in q:
                    new.extend([cur.left,cur.right])
                q=new
            else:
                for cur in q:
                    if cur:
                        res+=1
                    else:
                        q=[]
                        break
        return res
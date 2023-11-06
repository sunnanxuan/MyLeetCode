# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[[root.val]]
        q=[root]
        while q:
            new=[]
            arr=[]
            for c in q:
                if c.left:
                    new.append(c.left)
                    arr.append(c.left.val)
                if c.right:
                    new.append(c.right)
                    arr.append(c.right.val)
            if arr:
                res.append(arr)
            q=new
        res=list(reversed(res))
        return res

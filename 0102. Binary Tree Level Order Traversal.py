# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[[root.val]]
        q=[root]
        while q:
            new=[]
            arr=[]
            for n in q:
                if n.left:
                    new.append(n.left)
                    arr.append(n.left.val)
                if n.right:
                    new.append(n.right)
                    arr.append(n.right.val)
            q=new
            if arr:
                res.append(arr)
        return res
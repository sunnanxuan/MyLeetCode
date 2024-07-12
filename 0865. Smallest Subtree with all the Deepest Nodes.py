# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        arr=[]
        q=[root]
        while any(q):
            new=[]
            l=2**len(q)
            r=-1
            for i,n in enumerate(q):
                if n:
                    l=min(l,i)
                    r=max(r,i)
                    new.extend([n.left,n.right])
                else:new.extend([None,None])
            arr.append(q)
            q=new
        i=0
        while l!=r:
            i+=1
            l//=2
            r//=2
        m=len(arr)
        return arr[m-1-i][l]
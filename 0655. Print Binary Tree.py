# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        values=[]
        q=[root]
        res=[]
        while any(q):
            vals=[]
            new=[]
            for node in q:
                if not node:
                    vals.append('')
                    new.append(None)
                    new.append(None)
                else:
                    vals.append(str(node.val))
                    new.append(node.left)
                    new.append(node.right)
            q=new
            values.append(vals)
        n=0
        m=0
        while values:
            cur=values.pop()
            new_val=[]
            for c in cur:
                new_val.extend(['']*n)
                new_val.append(c)
                new_val.extend(['']*n)
                new_val.append('')
            new_val.pop()
            n+=(2**m)
            m+=1
            res.append(new_val)
        res.reverse()
        return res

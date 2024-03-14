# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=collections.defaultdict(int)
        def traverse(node):
            if node:
                dic[node.val]+=1
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        count=sorted(list(dic.items()),key=lambda x:x[1],reverse=True)
        res=[]
        m=count[0][1]
        for k,v in count:
            if v==m:
                res.append(k)
            else:
                break
        return res

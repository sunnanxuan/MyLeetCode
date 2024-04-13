# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        q=[root]
        while q:
            level=[]
            new=[]
            for node in q:
                level.append(node.val)
                if node.left:new.append(node.left)
                if node.right:new.append(node.right)
            res.append(sum(level)/len(level))
            q=new
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        arr=[]
        def add(sm,node):
            if not node:
                return
            if not node.left and not node.right:
                if sm+node.val==targetSum:
                    arr.append(node.val)
                    lst=copy.copy(arr)
                    res.append(lst)
                    arr.pop()
                    return
                else:
                    return
            else:
                arr.append(node.val)
                add(sm+node.val,node.left)
                add(sm+node.val,node.right)
                arr.pop()
        add(0,root)
        return res
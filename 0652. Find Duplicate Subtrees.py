# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen=set()
        visited=set()
        res=[]
        def traverse(node):
            if not node: return "^"
            else:
                string="$"+str(node.val)+"?"+traverse(node.left)+"@"+traverse(node.right)
                if string in seen and string not in visited:
                    res.append(node)
                    visited.add(string)
                seen.add(string)
                return string
        traverse(root)
        return res
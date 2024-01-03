# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic={}
        if p==root or q==root:
            return root
        def traverse(node,pre):
            if node:
                dic[node.val]=pre
                if node.left:
                    traverse(node.left,node)
                if node.right:
                    traverse(node.right,node)
        traverse(root,None)
        ancestor_p=[p]
        while dic[p.val]:
            ancestor_p.append(dic[p.val])
            p=dic[p.val]
        if q in ancestor_p:
            return q
        while dic[q.val]:
            if dic[q.val] in ancestor_p:
                return dic[q.val]
            else:
                q=dic[q.val]
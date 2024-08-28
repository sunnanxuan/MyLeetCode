# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        if root.val != voyage[0]: return [-1]
        res = []

        def match(node, arr):
            if not node.left and not node.right:
                return not arr
            elif not node.right:
                if not arr: return False
                if node.left.val == arr[0]:
                    return match(node.left, arr[1:])
            elif not node.left:
                if not arr: return False
                if node.right.val == arr[0]:
                    return match(node.right, arr[1:])
            else:

                if node.left.val not in arr or node.right.val not in arr: return False
                l = arr.index(node.left.val)
                r = arr.index(node.right.val)
                if l != 0 and r != 0:
                    return False
                elif l < r:
                    return match(node.left, arr[1:r]) and match(node.right, arr[r + 1:])
                else:
                    res.append(node.val)
                    return match(node.left, arr[l + 1:]) and match(node.right, arr[1:l])

        if match(root, voyage[1:]):
            return res
        else:
            return [-1]


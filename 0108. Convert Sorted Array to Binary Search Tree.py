# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        p = len(nums) // 2
        root = TreeNode(nums[p])
        if p > 0:
            root.left = self.sortedArrayToBST(nums[:p])
        if p < len(nums) - 1:
            root.right = self.sortedArrayToBST(nums[p + 1:])
        return root

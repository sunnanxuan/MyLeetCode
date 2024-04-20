# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums):
            if nums:
                m=max(nums)
                p=nums.index(m)
                l=nums[:p]
                r=nums[p+1:]
                root=TreeNode(m)
                root.left=construct(l)
                root.right=construct(r)
                return root
            else:
                return None

        return construct(nums)
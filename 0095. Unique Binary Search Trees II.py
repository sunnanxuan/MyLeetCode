# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums=[num for num in range(1,n+1)]
        memo={}
        def build(nums):
            if not nums:
                return [None]
            elif (nums[0],nums[-1]) in memo:
                return memo[(nums[0],nums[-1])]
            else:
                arr=[]
                for i in range(len(nums)):
                    left=build(nums[:i])
                    right=build(nums[i+1:])
                    for l in left:
                        for r in right:
                            node=TreeNode(nums[i])
                            node.left=l
                            node.right=r
                            arr.append(node)
                memo[(nums[0],nums[-1])]=arr
                return arr
        build(nums)
        return memo[(1,n)]
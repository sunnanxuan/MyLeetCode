class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sm=sum(list(set(nums)))
        return (sum(nums)-sm)//(len(nums)-len(list(set(nums))))
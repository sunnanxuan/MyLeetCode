class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p=bisect.bisect_left(nums,target)
        return p
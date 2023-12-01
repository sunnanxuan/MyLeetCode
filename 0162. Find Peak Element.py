class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        mx=max(nums)
        return nums.index(mx)
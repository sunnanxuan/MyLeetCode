class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        d=max(max(nums)-min(nums),2*k)
        return d-2*k
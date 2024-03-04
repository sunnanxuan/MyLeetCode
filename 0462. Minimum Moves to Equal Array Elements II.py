class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        m=len(nums)//2
        res=sum(abs(nums[m]-num) for num in nums)
        return res
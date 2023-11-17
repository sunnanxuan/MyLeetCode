class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_s=list(set(nums))
        s=sum(nums)
        m=s-sum(nums_s)
        return s-2*m
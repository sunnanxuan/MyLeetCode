class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return 2*sum(list(set(nums)))-sum(nums)
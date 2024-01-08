class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n={i for i in range(len(nums))}
        diff=list(n-set(nums))
        if diff:
            return diff[0]
        else:
            return len(nums)
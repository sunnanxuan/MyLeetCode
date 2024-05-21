class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        i = 0
        l = sum(nums[:i])
        r = sum(nums[i:])
        while i < len(nums):
            r -= nums[i]
            if l == r:
                return i
            else:
                l += nums[i]
                i += 1

        return -1

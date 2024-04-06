class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)
        l = 0
        r = len(nums) - 1
        while l < len(nums) and nums[l] == snums[l]:
            l += 1
        while r >= l and nums[r] == snums[r]:
            r -= 1
        return r - l + 1

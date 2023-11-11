class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        i = 0
        j = 1
        res = 0
        if not nums:
            return res
        while j < len(nums):
            if nums[j - 1] == nums[j] - 1:
                j += 1
            else:
                res = max(res, j - i)

                i = j
                j += 1
        res = max(res, j - i)
        return res
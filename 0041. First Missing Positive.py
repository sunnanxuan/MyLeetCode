class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                if i == 0 and nums[i] > 1:
                    return 1
                elif nums[i] - nums[i - 1] > 1:
                    if nums[i - 1] > 0:
                        return nums[i - 1] + 1
                    elif nums[i] > 1:
                        return 1
        return nums[-1] >= 0 and nums[-1] + 1 or 1

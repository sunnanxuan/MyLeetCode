class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[l] < nums[mid]:
                l = mid
            elif nums[l] > nums[mid]:
                r = mid

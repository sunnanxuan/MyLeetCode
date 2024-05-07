class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1

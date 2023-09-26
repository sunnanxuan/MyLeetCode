class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            print(l, r)
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif sum((nums[mid] > target, nums[l] <= target, nums[mid] < nums[l])) == 2:
                r = mid - 1
            else:
                l = mid + 1
        return -1

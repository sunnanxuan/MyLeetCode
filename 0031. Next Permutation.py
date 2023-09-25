class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                p = -1
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        p = j
                        break
                nums[:] = nums[:i - 1] + nums[p:p + 1] + sorted(nums[i - 1:p] + nums[p + 1:])
                change = True
                break
        if change == False:
            nums.sort()


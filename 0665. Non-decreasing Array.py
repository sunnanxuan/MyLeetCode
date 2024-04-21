class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        change = 0
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            else:
                if change == 1:
                    return False
                else:
                    if i == 0 or i + 2 == len(nums):
                        change += 1
                    else:
                        if nums[i] <= nums[i + 2] or nums[i - 1] <= nums[i + 1]:
                            change += 1
                        else:
                            return False
        return True


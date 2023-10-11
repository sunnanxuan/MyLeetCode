class Solution:
    def sortColors(self, nums: List[int]) -> None:
        o = t = -1
        for i in range(len(nums)):
            if i == 0 or nums[i] >= nums[i - 1]:
                if nums[i] == 2 and t == -1:
                    t = i
                elif nums[i] == 1 and o == -1:
                    o = i
            elif nums[i] == 0:
                j = i
                if t >= 0:
                    nums[j], nums[t] = nums[t], nums[j]
                    j = t
                    t += 1
                if o >= 0:
                    nums[j], nums[o] = nums[o], nums[j]
                    o += 1
            elif nums[i] == 1:
                j = i
                if t >= 0:
                    nums[j], nums[t] = nums[t], nums[j]
                    j = t
                    t += 1

                if o == -1:
                    o = j
        return nums

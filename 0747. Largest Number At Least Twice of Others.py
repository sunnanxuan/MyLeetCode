class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        new=sorted(nums)
        print
        if new[-1]>=new[-2]*2:return nums.index(new[-1])
        else:return -1

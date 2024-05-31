class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        arr = []
        mn = float('inf')
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > mn:
                return False
            mn = min(mn, nums[i])
        return True

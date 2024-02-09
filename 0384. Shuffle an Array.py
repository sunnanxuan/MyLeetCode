class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = copy.copy(nums)

    def reset(self) -> List[int]:
        self.nums = copy.copy(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
        shuffle(self.nums)
        return self.nums
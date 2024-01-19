class NumArray:

    def __init__(self, nums):
        self.sm = nums
        for i in range(1, len(nums)):
            self.sm[i] += self.sm[i - 1]

    def sumRange(self, i, j):
        if i == 0:
            return self.sm[j]
        else:
            return self.sm[j] - self.sm[i - 1]

class Solution:

    def __init__(self, nums: List[int]):
        self.ind = collections.defaultdict(list)
        for i, c in enumerate(nums):
            self.ind[c].append(i)

    def pick(self, target: int) -> int:
        return choice(self.ind[target])

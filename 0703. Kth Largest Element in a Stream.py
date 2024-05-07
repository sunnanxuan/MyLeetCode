class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.stream, val)
        if len(self.stream) > self.k:
            self.stream.pop(0)
        return self.stream[0]

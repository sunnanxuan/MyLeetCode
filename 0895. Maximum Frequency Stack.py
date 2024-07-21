class FreqStack:

    def __init__(self):
        self.frequent = collections.defaultdict(list)
        self.count = collections.defaultdict(int)

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.frequent[self.count[val]].append(val)

    def pop(self) -> int:
        k = max(self.frequent.keys())
        m = self.frequent[k].pop()
        if not self.frequent[k]: self.frequent.pop(k)
        self.count[m] -= 1
        return m
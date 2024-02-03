class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.ind = collections.defaultdict(list)

    def insert(self, val):

        self.nums.append(val)
        self.ind[val].append(len(self.nums) - 1)
        if len(self.ind[val]) >= 2:
            return False
        else:
            return True

    def remove(self, val):
        if not self.ind[val]:
            return False
        else:
            if val == self.nums[-1]:
                self.nums.pop()
                self.ind[val].pop()
            else:

                p = self.ind[val].pop()
                v = self.nums[-1]
                self.ind[v].pop()
                bisect.insort(self.ind[v], p)
                self.nums[p], self.nums[-1] = self.nums[-1], self.nums[p]
                self.nums.pop()
            return True

    def getRandom(self):
        res = choice(self.nums)
        return res
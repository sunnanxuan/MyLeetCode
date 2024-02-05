class SummaryRanges:

    def __init__(self):

        self.left = []
        self.right = []

    def addNum(self, val):
        l = bisect.bisect_right(self.left, val)
        r = bisect.bisect_left(self.right, val)
        if l != r:
            return
        else:
            if val + 1 in self.left and val - 1 in self.right:
                self.left.pop(l)
                self.right.pop(l - 1)
            elif val + 1 in self.left:
                self.left.pop(l)
                bisect.insort(self.left, val)
            elif val - 1 in self.right:
                self.right.pop(l - 1)
                bisect.insort(self.right, val)
            else:
                bisect.insort(self.left, val)
                bisect.insort(self.right, val)

    def getIntervals(self):
        self.intervals = []
        for i in range(len(self.left)):
            self.intervals.append([self.left[i], self.right[i]])
        return self.intervals
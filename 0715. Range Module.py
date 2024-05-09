class RangeModule:

    def __init__(self):
        self.interval = []

    def addRange(self, left: int, right: int) -> None:
        l = bisect.bisect_left(self.interval, left)
        r = bisect.bisect_right(self.interval, right)
        if l == r and l % 2 == 0:
            bisect.insort(self.interval, left)
            bisect.insort(self.interval, right)
        elif l < r:
            self.interval = self.interval[:l] + self.interval[r:]
            if l % 2 == 0 and r % 2 == 0:
                bisect.insort(self.interval, left)
                bisect.insort(self.interval, right)
            elif l % 2 == 0:
                bisect.insort(self.interval, left)
            elif r % 2 == 0:
                bisect.insort(self.interval, right)

    def queryRange(self, left: int, right: int) -> bool:
        l = bisect.bisect_right(self.interval, left)
        r = bisect.bisect_left(self.interval, right)
        if l == r and l % 2 == 1:
            return True
        else:
            return False

    def removeRange(self, left: int, right: int) -> None:
        l = bisect.bisect_left(self.interval, left)
        r = bisect.bisect_right(self.interval, right)
        if l == r and l % 2 == 1:
            bisect.insort(self.interval, left)
            bisect.insort(self.interval, right)
        elif l < r:
            self.interval = self.interval[:l] + self.interval[r:]
            if l % 2 == 1 and r % 2 == 1:
                bisect.insort(self.interval, left)
                bisect.insort(self.interval, right)
            elif l % 2 == 1:
                bisect.insort(self.interval, left)
            elif r % 2 == 1:
                bisect.insort(self.interval, right)



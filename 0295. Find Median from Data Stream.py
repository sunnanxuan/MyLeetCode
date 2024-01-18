class MedianFinder:

    def __init__(self):
        self.right = []
        self.left = []
        self.mid = []

    def addNum(self, num: int) -> None:
        if not self.mid:
            self.mid.append(num)
        elif len(self.mid) == 1:
            if num <= self.mid[0]:
                heapq.heappush(self.left, -1 * num)
                bisect.insort(self.mid, -1 * heapq.heappop(self.left))
            elif num > self.mid[0]:
                heapq.heappush(self.right, num)
                bisect.insort(self.mid, heapq.heappop(self.right))

        else:
            bisect.insort(self.mid, num)
            heapq.heappush(self.right, self.mid.pop())
            heapq.heappush(self.left, -1 * self.mid.pop(0))

    def findMedian(self) -> float:
        if len(self.mid) == 1:
            return self.mid[0]
        else:
            return sum(self.mid) / 2
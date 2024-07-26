class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = []
        while encoding:
            c = encoding.pop()
            m = encoding.pop()
            self.arr.append([m, c])

    def next(self, n: int) -> int:
        while n:
            if not self.arr:
                return -1
            else:
                m, c = self.arr.pop()
                if m >= n:
                    m -= n
                    if m: self.arr.append([m, c])
                    return c
                else:
                    n -= m
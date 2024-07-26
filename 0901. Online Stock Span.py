class StockSpanner:

    def __init__(self):
        self.span = []

    def next(self, price: int) -> int:
        s = 1
        while self.span and self.span[-1][0] <= price:
            c, n = self.span.pop()
            s += n
        self.span.append((price, s))
        return s

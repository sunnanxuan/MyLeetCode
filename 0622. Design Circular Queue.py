class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.n = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.n == self.k:
            return False
        else:
            self.queue.append(value)
            self.n += 1
            return True

    def deQueue(self) -> bool:
        if self.n == 0:
            return False
        else:
            self.queue.pop(0)
            self.n -= 1
            return True

    def Front(self) -> int:
        if self.n == 0:
            return -1
        else:
            return self.queue[0]

    def Rear(self) -> int:
        if self.n == 0:
            return -1
        else:
            return self.queue[-1]

    def isEmpty(self) -> bool:
        return bool(self.n == 0)

    def isFull(self) -> bool:
        return bool(self.n == self.k)
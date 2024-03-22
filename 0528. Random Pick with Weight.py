class Solution:

    def __init__(self, w: List[int]):
        self.ind = []
        self.w = w
        for i in range(len(w)):
            self.ind.append(i)

    def pickIndex(self) -> int:
        return choices(self.ind, self.w, k=1)[0]

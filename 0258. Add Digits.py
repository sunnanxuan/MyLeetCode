class Solution:
    def addDigits(self, num: int) -> int:
        n = str(num)
        while len(n) > 1:
            sm = 0
            for c in n:
                sm += int(c)
            n = str(sm)
        return int(n)

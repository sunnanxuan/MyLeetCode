class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a ** 2 <= c:
            if int((c - a ** 2) ** 0.5) ** 2 == c - a ** 2:
                return True
            else:
                a += 1
        return False

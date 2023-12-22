class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        if ax1 >= bx2 or bx1 >= ax2 or ay2 <= by1 or by2 <= ay1:
            return area_a + area_b
        else:
            x = [ax1, ax2, bx1, bx2]
            x.sort()
            y = [ay1, ay2, by1, by2]
            y.sort()
            area = (x[2] - x[1]) * (y[2] - y[1])
            return area_a + area_b - area

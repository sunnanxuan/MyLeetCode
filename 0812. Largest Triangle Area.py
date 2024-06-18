class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def compute(a, b, c):
            x1, y1 = a
            x2, y2 = b
            x3, y3 = c
            sq = 0.5 * abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
            return sq

        return max([compute(a, b, c) for a, b, c in itertools.combinations(points, 3)])
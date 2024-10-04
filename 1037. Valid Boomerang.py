class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = points
        if a == b or b == c or a == c: return False
        return (a[0] - b[0]) * (b[1] - c[1]) != (a[1] - b[1]) * (b[0] - c[0])


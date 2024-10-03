class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        mx = z - x - 2
        if y - x == z - y == 1:
            mn = 0
        elif y - x <= 2 or z - y <= 2:
            mn = 1
        else:
            mn = 2
        return [mn, mx]


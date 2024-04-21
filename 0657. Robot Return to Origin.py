class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h = v = 0
        for c in moves:
            if c == 'R':
                h += 1
            elif c == 'L':
                h -= 1
            elif c == 'U':
                v -= 1
            elif c == 'D':
                v += 1
        return h == v == 0

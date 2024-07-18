class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        d = 0
        x = y = 0
        obs = {tuple(o) for o in obstacles}
        res = 0
        for c in commands:
            if c == -1:
                d += 1
                d %= 4
            elif c == -2:
                d += 3
                d %= 4
            else:
                for i in range(c):
                    r, c = direction[d]
                    if (x + r, y + c) not in obs:
                        x += r
                        y += c
                    else:
                        break
                res = max(res, x ** 2 + y ** 2)
        return res




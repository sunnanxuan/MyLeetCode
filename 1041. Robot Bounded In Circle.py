class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i = j = 0
        d = 0
        direction = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
        for c in instructions:
            if c == 'G':
                i += direction[d][0]
                j += direction[d][1]
            elif c == 'L':
                d -= 1
                d %= 4
            elif c == 'R':
                d += 1
                d %= 4
        return (i == 0 and j == 0) or d != 0



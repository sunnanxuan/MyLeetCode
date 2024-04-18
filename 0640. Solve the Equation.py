class Solution:
    def solveEquation(self, equation: str) -> str:
        l, r = equation.split('=')
        if l == r:
            return "Infinite solutions"
        nums = 0
        xs = 0
        for s in [l, r]:
            if s == l:
                pre = 1
            else:
                pre = -1
            i = 0
            pos = 1
            while i < len(s):
                if s[i] == '+':
                    pos = 1
                    i += 1
                elif s[i] == '-':
                    pos = -1
                    i += 1
                elif s[i] == 'x':
                    xs += (-1 * pre * pos * 1)
                    i += 1
                elif s[i].isdigit():
                    j = i + 1
                    while j < len(s) and s[j].isdigit():
                        j += 1
                    if j < len(s) and s[j] == 'x':
                        xs += (-1 * pre * pos * int(s[i:j]))
                        i = j + 1
                    else:
                        nums += (pre * pos * int(s[i:j]))
                        i = j
        if nums == 0 and xs == 0:
            return "Infinite solutions"
        elif xs == 0:
            return "No solution"
        else:
            x = nums // xs
            return 'x={}'.format(x)


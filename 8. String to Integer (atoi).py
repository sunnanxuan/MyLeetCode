class Solution:
    def myAtoi(self, s: str) -> int:
        positive = 0
        i = 0
        s = s.lstrip()
        l = len(s)
        lst = []
        while i < l:
            if s[i] in "+-":
                if positive == 0:
                    if s[i] == '-':
                        positive = -1
                    elif s[i] == '+':
                        positive = 1
                else:
                    break
            elif s[i].isdigit():
                lst.append(s[i])
                if positive == 0:
                    positive = 1

            else:
                break
            i += 1
        if positive == 0:
            positive = 1
        if not lst: return 0
        res = int("".join(lst)) * positive
        if res >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res <= -2 ** 31:
            return -2 ** 31
        else:
            return res

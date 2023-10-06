class Solution:
    def isNumber(self, s: str) -> bool:
        dot = e = False
        n = 0
        m = 1
        for i in range(len(s)):
            if s[i] == '-' or s[i] == '+':
                if i == 0 or s[i - 1] in 'eE':
                    continue
                else:
                    return False
            elif s[i] == 'e' or s[i] == 'E':
                if e:
                    return False
                else:
                    e = True
                    dot = True
                    m = 0
            elif s[i] == '.':
                if dot:
                    return False
                else:
                    dot = True
            elif s[i] in '0123456789':
                if not e:
                    n += 1
                else:
                    m += 1
            else:
                return False
        if n == 0 or m == 0:
            return False
        else:
            return True


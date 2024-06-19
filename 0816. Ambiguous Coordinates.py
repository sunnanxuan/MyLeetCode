class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def validnum(s):
            if '.' not in s:
                return str(int(s)) == s
            else:
                if s[-1] == '0' or (s[0] == '0' and s[1] != '.'):
                    return False
                else:
                    return True

        def addpoint(s):
            res = []
            if validnum(s): res.append(s)
            for i in range(1, len(s)):
                c = s[:i] + '.' + s[i:]
                if validnum(c): res.append(c)
            return res

        res = []
        s = s[1:-1]
        for i in range(1, len(s)):
            L = addpoint(s[:i])
            R = addpoint(s[i:])
            for l in L:
                for r in R:
                    res.append('({}, {})'.format(l, r))
        return res

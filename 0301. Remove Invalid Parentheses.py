class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        i = 0
        while i < len(s) and s[i] == ')':
            i += 1
        j = len(s) - 1
        while j >= 0 and s[j] == '(':
            j -= 1
        s = s[i:j + 1]

        def remove(s, l, r):
            q = {''}
            p = 0
            i = 0
            while i < len(s):
                if s[i] == l:
                    p += 1
                elif s[i] == r:
                    p -= 1
                i += 1
                new = set()
                for c in q:
                    new.add(c + s[i - 1])
                    q = new
                if p < 0:
                    p += 1
                    new = set()
                    for c in q:
                        j = 0
                        while j < len(c):
                            if c[j] == l:
                                j += 1
                            elif c[j] == r:
                                k = j
                                while k < len(c) and c[k] == r: k += 1
                                new.add(c[:j] + c[j:k - 1] + c[k:])
                                j = k
                            else:
                                j += 1
                    q = new
            return q

        arr = remove(s, '(', ')')
        res = []
        for string in arr:
            lst = remove(string[::-1], ')', '(')
            for c in lst: res.append(c[::-1])
        return res

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        expression = expression.replace('(', '( ')
        expression = expression.replace(')', ' )')
        dic = {}
        for i in range(len(evalvars)):
            dic[evalvars[i]] = str(evalints[i])
        s = expression.split()
        for i, c in enumerate(s):
            if c in dic: s[i] = dic[c]

        def calculator(i):
            sm = collections.defaultdict(int)
            stack = []
            pre = '+'
            while i < len(s):
                if s[i].isdigit() or (s[i][0] == '-' and s[i][1:].isdigit()):
                    if pre == '+':
                        stack.append(('', s[i]))
                    elif pre == '-':
                        stack.append(('', str(-1 * int(s[i]))))
                    elif pre == '*':
                        new = []
                        for e, n in stack:
                            n = str(int(n) * int(s[i]))
                            new.append((e, n))
                        stack = new
                    i += 1
                elif s[i].islower():
                    if pre == '+':
                        stack.append((s[i], '1'))
                    elif pre == '-':
                        stack.append((s[i], '-1'))
                    elif pre == '*':
                        new = []
                        for e, n in stack:
                            if e == '':new.append((s[i], n))
                            else:
                                v = [s[i]] + e.split('*')
                                v.sort()
                                v = '*'.join(v)
                                new.append((v, n))
                        stack = new
                    i += 1

                elif s[i] == '(':
                    r, j = calculator(i + 1)
                    if pre == '*':
                        new = []
                        for e, n in stack:
                            for c, m in r:
                                nn = str(int(n) * int(m))
                                if e == '':
                                    new.append((c, nn))
                                elif c == '':
                                    new.append((e, nn))
                                else:
                                    v = c.split('*') + e.split('*')
                                    v.sort()
                                    v = '*'.join(v)
                                    new.append((v, nn))
                        stack = new

                    elif pre == '-':
                        for c, m in r:
                            stack.append((c, str(-1 * int(m))))
                    else:
                        stack = r
                    i = j + 1

                elif s[i] == ')':
                    while stack:
                        e, n = stack.pop()
                        sm[e] += int(n)
                    arr = [(k, str(sm[k])) for k in sm]
                    return [arr, i]
                elif s[i] in '+-':
                    pre = s[i]
                    while stack:
                        e, n = stack.pop()
                        sm[e] += int(n)
                    i += 1
                elif s[i] == '*':
                    pre = '*'
                    i += 1

            while stack:
                e, n = stack.pop()
                sm[e] += int(n)
            res = []
            keys = list(sm.keys())
            keys.sort(key=lambda x: (-1 * x.count('*'), x, sm[x]))
            t = 0
            for k in keys:
                if sm[k] == 0: continue
                if k == '':
                    t = str(sm[k])
                else:
                    res.append(str(sm[k]) + '*' + k)
            if t: res.append(t)
            return res

        return calculator(0)


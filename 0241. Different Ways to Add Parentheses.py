class Solution:
    def diffWaysToCompute(self, input):
        def operation(m1, m2, op):
            if op == '+':
                return m1 + m2
            elif op == '-':
                return m1 - m2
            elif op == '*':
                return m1 * m2

        exp = []
        i = j = 0
        while j < len(input):
            while j < len(input) and input[j].isdigit():
                j += 1
            exp.append(input[i:j])
            if j < len(input):
                exp.append(input[j])
            j += 1
            i = j
        q = [[int(exp.pop())]]
        while len(exp) > 1:

            e = exp.pop()
            if e in '+-*':
                for lst in q:
                    lst.append(e)
            else:
                new = []
                for lst in q:
                    lst.append(int(e))
                    new.append(lst)
                    c = copy.copy(lst)
                    while len(c) > 1:
                        m1 = c.pop()
                        op = c.pop()
                        m2 = c.pop()
                        c.append(operation(m1, m2, op))
                        new.append(c)
                        c = copy.copy(c)
                q = new
        res = []
        for lst in q:
            if exp:
                lst.append(int(exp[-1]))
            while len(lst) > 1:
                m1 = lst.pop()
                op = lst.pop()
                m2 = lst.pop()
                lst.append(operation(m1, m2, op))
            res.append(lst[-1])

        return res
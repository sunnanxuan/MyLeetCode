class Solution:
    def evaluate(self, expression: str) -> int:
        expression = expression.replace(')', ' )')
        exp = expression.split()
        dic = collections.defaultdict(list)

        def find(i):
            if exp[i].isdigit() or (exp[i][0] == '-' and exp[i][1:].isdigit()):
                return exp[i]
            elif exp[i] in dic:
                return dic[exp[i]][-1]
            elif exp[i] == '(add':
                add(i)
                return exp[i]
            elif exp[i] == '(mult':
                mult(i)
                return exp[i]
            elif exp[i] == '(let':
                let(i)
                return exp[i]

        def let(i):
            variable = []
            j = i + 1
            while exp[j] not in {'(add', '(mult', '(let'} and exp[j + 1] != ')':
                k = exp[j]
                v = find(j + 1)
                variable.append(k)
                dic[k].append(v)
                j += 2
            new = find(j)
            e = j
            while e < len(exp) and exp[e] != ')':
                e += 1
            exp[i:e + 1] = [new]
            for c in variable: dic[c].pop()

        def add(i):
            j = i + 1
            m1 = find(j)
            j += 1
            m2 = find(j)
            exp[i:j + 2] = [str(int(m1) + int(m2))]

        def mult(i):
            j = i + 1
            m1 = find(j)
            j += 1
            m2 = find(j)
            exp[i:j + 2] = [str(int(m1) * int(m2))]

        return int(find(0))

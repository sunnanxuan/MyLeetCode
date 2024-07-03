class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)

        def split(m1, m2, p):
            if (len(m1) > 1 and m1[0] == '0') or (len(m2) > 1 and m2[0] == '0'): return [False, []]
            if p == n: return [True, []]
            c = str(int(m1) + int(m2))
            if int(c) >= 2 ** 31: return [False, []]
            l = len(c)
            if c == num[p:p + l]:
                r, ind = split(m2, c, p + l)
                if r:
                    return [True, [p + l] + ind]
                else:
                    return [False, []]
            else:
                return [False, []]

        for i in range(1, n // 2 + 1):
            for j in range(i + 1, n - i + 1):
                m1 = num[:i]
                m2 = num[i:j]

                r, ind = split(m1, m2, j)
                if r:
                    ind = [i, j] + ind
                    res = []
                    pre = 0
                    for p in ind:
                        res.append(int(num[pre:p]))
                        pre = p
                    return res
        return []



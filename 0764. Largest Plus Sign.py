class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        v = collections.defaultdict(list)
        h = collections.defaultdict(list)
        for r, c in mines:
            bisect.insort(v[c], r)
            bisect.insort(h[r], c)
        res = 0
        for i in range(n):
            for j in range(n):
                if j not in v:
                    u = i + 1
                    d = n - i
                else:
                    if i in v[j]:
                        u = d = 0
                    else:
                        k = bisect.bisect(v[j], i)
                        if k == 0:
                            u = i + 1
                        elif k > 0:
                            u = i - v[j][k - 1]
                        if k == len(v[j]):
                            d = n - i
                        if k < len(v[j]):
                            d = v[j][k] - i

                if i in h:
                    if j in h[i]:
                        l = r = 0
                    else:
                        p = bisect.bisect(h[i], j)
                        if p == 0:
                            l = j + 1
                        elif p > 0:
                            l = j - h[i][p - 1]
                        if p < len(h[i]):
                            r = h[i][p] - j
                        else:
                            r = n - j
                else:
                    l = j + 1
                    r = n - j
                res = max(res, min(u, d, l, r))
        return res

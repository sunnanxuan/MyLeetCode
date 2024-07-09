class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = set()
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
        dic = collections.defaultdict(list)
        for x1, y1, x2, y2 in rectangles:
            for x in xs:
                if x1 <= x < x2:
                    p1 = bisect.bisect_right(dic[x], y1)
                    p2 = bisect.bisect_left(dic[x], y2)
                    if p1 == p2:
                        if p1 % 2:
                            continue
                        else:
                            bisect.insort(dic[x], y1)
                            bisect.insort(dic[x], y2)
                    else:
                        if p1 % 2 == 0 and p2 % 2 == 0:
                            dic[x][p1:p2] = [y1, y2]
                        elif p1 % 2 == 0 and p2 % 2:
                            dic[x][p1:p2] = [y1]
                        elif p1 % 2 and p2 % 2 == 0:
                            dic[x][p1:p2] = [y2]
                        else:
                            dic[x][p1:p2] = []

        xs = sorted(list(xs))
        res = 0
        mod = 10 ** 9 + 7
        i = 0
        while i < len(xs) - 1:
            l = xs[i]
            r = xs[i + 1]
            if l in dic:
                h = 0
                for j in range(0, len(dic[l]), 2):
                    h += (dic[l][j + 1] - dic[l][j])
                s = (r - l) * h % mod
                res += s
            i += 1
        res %= mod
        return res



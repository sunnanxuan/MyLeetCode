class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        point = []
        res = [0]
        dic = {}
        for l, h in positions:
            r = l + h
            pl = bisect.bisect_right(point, l)
            pr = bisect.bisect_left(point, r)
            if pl == pr:
                if pl == 0 or pr == len(point) or (
                        dic[point[pl - 1]][1] < point[pl - 1] and dic[point[pr]][1] > point[pr]):
                    if l not in dic or h > dic[l][0]: dic[l] = [h, r]
                    if r not in dic or h > dic[r][0]: dic[r] = [h, l]
                    res.append(max(res[-1], h))
                else:
                    ch = h + min(dic[point[pl - 1]][0], dic[point[pl]][0])
                    dic[l] = [ch, r]
                    dic[r] = [ch, l]
                    res.append(max(res[-1], ch))
            else:
                d = 0
                for i in range(pr - pl):
                    c = point.pop(pl)
                    d = max(d, dic[c][0])
                    dic.pop(c)
                ch = h + d
                dic[l] = [ch, r]
                dic[r] = [ch, l]
                res.append(max(res[-1], ch))
            if l not in point:
                bisect.insort(point, l)
            if r not in point:
                bisect.insort(point, r)
        return res[1:]



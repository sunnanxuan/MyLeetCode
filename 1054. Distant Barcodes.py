class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = collections.Counter(barcodes)
        arr = sorted(list(count.items()), key=lambda x: x[1])
        c, n = arr.pop()
        lst = [[c] for i in range(n)]
        if n * 2 > len(barcodes): n -= 1
        i = 0
        while arr:
            c, m = arr.pop()
            while m:
                lst[i].append(c)
                m -= 1
                i += 1
                if i == n: i = 0
        res = []
        for l in lst:
            res.extend(l)
        return res


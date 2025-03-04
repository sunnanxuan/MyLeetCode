class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = 0
        minimum = None
        maximum = None
        sm = 0
        dic = {}
        arr = []
        for i, c in enumerate(count):
            n += c
            sm += (i * c)
            if c != 0:
                dic[n - 1] = i
                arr.append(n - 1)
                if minimum == None:
                    minimum = i
                maximum = i

        mean = sm / n
        if n % 2:
            l = n // 2
            r = n // 2
        else:
            l = n // 2 - 1
            r = n // 2
        pl = bisect.bisect_left(arr, l)
        pr = bisect.bisect_left(arr, r)
        median = (dic[arr[pl]] + dic[arr[pr]]) / 2

        m = max(count)
        mode = count.index(m)
        return [minimum, maximum, mean, median, mode]

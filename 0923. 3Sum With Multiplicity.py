class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)

        def count(t, i):
            dic = collections.Counter(arr[i + 1:])
            res = 0
            used = set()
            for k in dic:
                if k * 2 == t and dic[k] >= 2:
                    if dic[k] == 2:
                        res += 1
                    else:
                        res += (math.factorial(dic[k]) // (math.factorial(dic[k] - 2) * 2))
                    used.add(k)
                elif k not in used and k != t - k and t - k in dic:
                    res += dic[k] * dic[t - k]
                    used.add(t)
                    used.add(t - k)
            return res

        arr.sort()
        mod = 10 ** 9 + 7
        res = 0
        for i in range(n - 2):
            res += count(target - arr[i], i)
            res %= mod
        return res

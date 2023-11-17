class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = 1
        n = 1
        cur = 1
        pre = 2 * 10 ** 4 + 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                cur += 1
                res += cur
                n = 1
                pre = 2 * 10 ** 4 + 1
            elif ratings[i] < ratings[i - 1]:
                if cur == 1:
                    if n + 1 == pre:
                        n += 1
                        pre = 2 * 10 ** 4 + 1
                    res += (1 + n)
                    n += 1
                else:
                    res += 1
                    pre = cur
                    cur = 1
                    n = 1

            elif ratings[i] == ratings[i - 1]:
                cur = 1
                res += 1
                n = 1
                pre = 2 * 10 ** 4 + 1
        return res
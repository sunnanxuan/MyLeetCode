class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hp = [1]
        res = 0
        k = 0
        while k < n:
            num = heapq.heappop(hp)
            while num == res:
                num = heapq.heappop(hp)
            res = num
            k += 1
            for c in [2, 3, 5]:
                heapq.heappush(hp, num * c)
        return res

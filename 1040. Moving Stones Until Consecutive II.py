class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        mx = stones[-1] - stones[0] - n + 1 - min(stones[-1] - stones[-2] - 1, stones[1] - stones[0] - 1)
        m = 0
        for i in range(n):
            l = stones[i]
            r = l + n - 1
            p = bisect.bisect_right(stones, r)
            if stones[p - 1] != r and ((i == 0 and p >= n - 1) or (i <= 1 and p == n)):
                continue
            else:
                m = max(m, p - i)
        mn = n - m
        return [mn, mx]



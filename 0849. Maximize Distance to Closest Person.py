class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        inds = []
        for i, c in enumerate(seats):
            if c == 1:
                inds.append(i)
        res = inds[0]
        for i in range(len(inds) - 1):
            res = max(res, (inds[i + 1] - inds[i]) // 2)
        res = max(res, len(seats) - 1 - inds[-1])
        return res

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = set()
        for i in range(1, 10 - k):
            q.add(str(i))
        for i in range(max(k, 1), 10):
            q.add(str(i))

        for i in range(n - 1):
            new = set()
            for m in q:
                if int(m[-1]) >= k:
                    new.add(m + str(int(m[-1]) - k))
                if int(m[-1]) + k <= 9:
                    new.add(m + str(int(m[-1]) + k))
            q = new
        res = list(map(int, q))
        return res

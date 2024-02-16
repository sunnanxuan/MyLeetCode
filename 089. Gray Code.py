class Solution:
    def grayCode(self, n: int) -> List[int]:
        q = [0]
        for i in range(n):
            new = copy.copy(q[::-1])
            for m in new:
                q.append(m + 2 ** i)
        return q

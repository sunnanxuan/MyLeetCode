class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1, 1])
        for i in range(2, numRows):
            q = res[-1]
            new = [1]
            for j in range(1, i):
                new.append(q[j - 1] + q[j])
            new.append(1)
            res.append(new)
        return res

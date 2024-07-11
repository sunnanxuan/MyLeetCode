class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for r in grid:
            if r[0] == 0:
                for j in range(n):
                    if r[j] == 0:
                        r[j] = 1
                    else:
                        r[j] = 0
        dic = {i: ['1'] for i in range(m)}
        for j in range(1, n):
            z = []
            o = []
            for i in range(m):
                if grid[i][j] == 1:
                    o.append(i)
                else:
                    z.append(i)
            if len(z) > len(o):
                for p in z:
                    dic[p].append('1')
                for p in o:
                    dic[p].append('0')
            else:
                for p in z:
                    dic[p].append('0')
                for p in o:
                    dic[p].append('1')
        res = 0
        for i in dic:
            res += int(''.join(dic[i]), 2)
        return res

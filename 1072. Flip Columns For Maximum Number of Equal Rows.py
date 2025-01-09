class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        dic = collections.defaultdict(int)
        for r in matrix:
            c = map(str, r)
            dic[int(''.join(c), 2)] += 1
        res = 0
        lst = list(dic.keys())
        for k in lst:
            res = max(res, dic[k] + dic[2 ** n - 1 - k])
        return res


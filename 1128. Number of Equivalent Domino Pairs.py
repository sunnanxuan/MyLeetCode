class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        for d in dominoes:
            dic[tuple(sorted(d))] += 1
        res = 0
        for k in dic:
            if dic[k] > 1:
                res += (dic[k] * (dic[k] - 1) // 2)
        return res

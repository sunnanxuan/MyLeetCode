class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tru = collections.defaultdict(list)
        trued = collections.defaultdict(list)
        for a, b in trust:
            tru[a].append(b)
            trued[b].append(a)
        for i in range(1, n + 1):
            if len(trued[i]) == n - 1 and i not in tru:
                return i
        return -1

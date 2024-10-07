class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        connected = collections.defaultdict(set)
        ban = collections.defaultdict(set)
        for a, b in paths:
            connected[a].add(b)
            connected[b].add(a)
        res = []
        for i in range(1, n + 1):
            for f in range(1, 5):
                if f not in ban[i]:
                    res.append(f)
                    for c in connected[i]:
                        ban[c].add(f)
                    break
        return res




class WordFilter:

    def __init__(self, words: List[str]):
        visited = set()
        self.prefix = collections.defaultdict(set)
        self.suffix = collections.defaultdict(set)
        for i in range(len(words) - 1, -1, -1):
            w = words[i]
            if w in visited: continue
            for j in range(1, len(w) + 1):
                self.prefix[w[:j]].add(i)
                self.suffix[w[-1 * (j):]].add(i)
            visited.add(w)

    def f(self, pref: str, suff: str) -> int:
        p = self.prefix[pref]
        s = self.suffix[suff]
        res = p & s
        if not res:
            return -1
        else:
            return max(res)
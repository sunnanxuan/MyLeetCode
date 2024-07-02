class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(a, b):
            c = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    c += 1
                if c > 2: return False
            return True

        inds = {i for i in range(len(strs))}
        res = 0
        dic = collections.defaultdict(set)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if check(strs[i], strs[j]):
                    dic[i].add(j)
                    dic[j].add(i)
        visited = set()
        while inds:
            c = inds.pop()
            q = {c}
            visited.add(c)
            res += 1
            while q:
                new = set()
                for p in q:
                    for n in dic[p]:
                        if n not in visited:
                            new.add(n)
                            inds.discard(n)
                            visited.add(n)
                q = new
        return res


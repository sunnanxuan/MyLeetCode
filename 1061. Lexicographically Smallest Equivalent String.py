class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def root(c):
            return c if parent[c] == c else root(parent[c])
        parent = {s: s for s in string.ascii_lowercase}
        for a, b in zip(s1, s2):
            p1, p2 = root(a), root(b)
            if p1 <= p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        return ''.join(root(s) for s in baseStr)
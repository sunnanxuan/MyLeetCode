class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        dias_r = collections.defaultdict(int)
        dias_l = collections.defaultdict(int)
        lights = set()
        for r, c in lamps:
            if (r, c) in lights: continue
            lights.add((r, c))
            rows[r] += 1
            cols[c] += 1
            dias_l[r - c] += 1
            dias_r[r + c] += 1

        ans = []
        for r, c in queries:
            if rows[r] > 0 or cols[c] > 0 or dias_l[r - c] > 0 or dias_r[r + c] > 0:
                ans.append(1)
            else:
                ans.append(0)
            qset = {(r, c), (r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c + 1),
                    (r + 1, c), (r + 1, c - 1)}
            off = lights & qset
            for i, j in off:
                rows[i] -= 1
                cols[j] -= 1
                dias_l[i - j] -= 1
                dias_r[i + j] -= 1
                lights.discard((i, j))
        return ans


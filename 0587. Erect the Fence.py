class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        memo = {}

        def slope(i, j):
            if (i, j) in memo:return memo[(i, j)]
            else:
                if trees[i][0] == trees[j][0]:memo[(i, j)] = memo[(j, i)] = float('inf')
                else:memo[(i, j)] = memo[(j, i)] = (trees[i][1] - trees[j][1]) / (trees[i][0] - trees[j][0])
                return memo[(i, j)]

        trees.sort(key=lambda x: (x[0], x[1]))
        res = []
        visited = set()
        res.append(trees[0])
        visited.add(tuple(trees[0]))
        end = trees[-1][0]
        i = 0
        d = 'R'
        while d == 'R' or i != 0:
            nxt = [float('inf'), []]
            if d == 'R':
                p = [n for n in range(i + 1, len(trees))]
            elif d == 'L':
                p = [n for n in range(i)]
            for j in p:
                s = slope(i, j)
                if s < nxt[0]:
                    nxt = [s, [j]]
                elif s == nxt[0]:
                    nxt[1].append(j)
            for k in nxt[1]:
                if tuple(trees[k]) not in visited:
                    res.append(trees[k])
                    visited.add(tuple(trees[k]))
            if d == 'R':i = max(nxt[1], default=i)
            else:i = min(nxt[1])
            if d == 'R' and i == len(trees) - 1:d = 'L'
        return res


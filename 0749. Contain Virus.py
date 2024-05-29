class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m = len(isInfected)
        n = len(isInfected[0])
        res = [0]
        killed = set()
        killed.add('&')

        def infect(i, j, nxt, visited, area):
            visited.add((i, j))
            area.add((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    if isInfected[x][y] == 0:
                        nxt.append((x, y))
                    elif isInfected[x][y] == 1:
                        infect(x, y, nxt, visited, area)

        def count(isInfected, killed):
            virus = []
            visited = set()
            visited |= killed
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        area = set()
                        nxt = []
                        infect(i, j, nxt, visited, area)
                        if nxt: virus.append([nxt, area])
            if virus:
                virus.sort(key=lambda x: len(set(x[0])))
                cur = virus.pop()
                res[0] += len(cur[0])
                killed |= cur[1]
                new = []
            if virus:
                for vir, _ in virus:
                    for i, j in vir: isInfected[i][j] = 1
                count(isInfected, killed)

        count(isInfected, killed)
        return res[0]




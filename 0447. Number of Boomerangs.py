class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        distance = collections.defaultdict(dict)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                l = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if l not in distance[i]:
                    distance[i][l] = [j]
                else:
                    distance[i][l].append(j)
                if l not in distance[j]:
                    distance[j][l] = [i]
                else:
                    distance[j][l].append(i)
        res = 0
        for p in distance:
            for d in distance[p]:
                n = len(distance[p][d])
                res += n * (n - 1)
        return res

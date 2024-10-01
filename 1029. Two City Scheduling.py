class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        for i in range(len(costs)):
            arr.append((costs[i][0] - costs[i][1], i))
        arr.sort()
        res = 0
        for i in range(len(costs) // 2):
            res += costs[arr[i][1]][0]
        for i in range(len(costs) // 2, len(costs)):
            res += costs[arr[i][1]][1]
        return res



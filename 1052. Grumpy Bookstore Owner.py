class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = 0
        uns = []
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
                uns.append(0)
            else:
                uns.append(customers[i])

        sm = sum(uns[:minutes])
        mx = sm
        for j in range(len(uns) - minutes):
            sm -= uns[j]
            sm += uns[j + minutes]
            mx = max(sm, mx)
        res += mx
        return res



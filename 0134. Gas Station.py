class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        lst = [gas[i] - cost[i] for i in range(len(gas))]
        sm = sum(lst)
        if sm < 0:
            return -1
        i = 0
        while i < len(gas):
            if lst[i] < 0:
                i += 1
            elif lst[i] >= 0:
                l = 1
                m = lst[i]
                j = i
                while l < len(gas):
                    if j + 1 < len(gas):
                        j += 1
                    else:
                        j = 0
                    m += lst[j]
                    if m >= 0:
                        l += 1
                    else:
                        break
                if l == len(gas):
                    return i
                elif j < len(gas):
                    i = j
                else:
                    return -1
        return -1

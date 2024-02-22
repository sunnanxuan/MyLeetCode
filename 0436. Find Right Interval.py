class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ind = {}
        starts = []
        ends = []
        res = []
        for i, inter in enumerate(intervals):
            ind[inter[0]] = i
            starts.append(inter[0])
            ends.append(inter[1])
        starts.sort()
        for e in ends:
            p = bisect.bisect_left(starts, e)
            if p == len(starts):
                res.append(-1)
            else:
                res.append(ind[starts[p]])
        return res


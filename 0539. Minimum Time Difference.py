class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        h = int(timePoints[0][:2])
        m = int(timePoints[0][3:])
        res = (h + 24 - int(timePoints[-1][:2])) * 60 - int(timePoints[-1][3:]) + m

        for t in timePoints[1:]:
            res = min(res, (int(t[:2]) - h) * 60 - m + int(t[3:]))
            h = int(t[:2])
            m = int(t[3:])
        return res

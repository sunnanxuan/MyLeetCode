class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        lst = sorted(firstList + secondList)
        pre = -1
        res = []
        for s, e in lst:
            if s <= pre:
                res.append([s, min(pre, e)])
            pre = max(e, pre)
        return res

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        for m in matrix:
            lst.extend(m)
        heapq.heapify(lst)
        return list(heapq.nsmallest(k, lst))[-1]

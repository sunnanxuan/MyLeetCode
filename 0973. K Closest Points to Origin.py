class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x ** 2 + y ** 2, [x, y]))
        res = [p[1] for p in heapq.nsmallest(k, heap)]
        return res

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for w in stones:
            heapq.heappush(heap, -w)

        while len(heap) > 1:
            w1 = -1 * heapq.heappop(heap)
            w2 = -1 * heapq.heappop(heap)
            if w1 > w2:
                heapq.heappush(heap, w2 - w1)

        return -1 * heap.pop() if heap else 0

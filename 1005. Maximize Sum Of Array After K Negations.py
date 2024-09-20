class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(k):
            cur = heapq.heappop(nums)
            heapq.heappush(nums, -1 * cur)
        return sum(nums)

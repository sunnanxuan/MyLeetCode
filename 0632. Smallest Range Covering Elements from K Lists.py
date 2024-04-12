class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        heapq.heapify(heap)
        inds = collections.defaultdict(list)
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i][0])
            inds[nums[i][0]].append(i)
            nums[i].pop(0)
        mn = heapq.nsmallest(1, heap)[0]
        mx = heapq.nlargest(1, heap)[0]
        inter = mx - mn
        res = [mn, mx]
        m = heapq.heappop(heap)
        j = inds[m].pop()
        while nums[j]:
            p = nums[j].pop(0)
            heapq.heappush(heap, p)
            inds[p].append(j)
            mn = heapq.nsmallest(1, heap)[0]
            mx = heapq.nlargest(1, heap)[0]
            if mx - mn < inter:
                inter = mx - mn
                res = [mn, mx]
            m = heapq.heappop(heap)
            j = inds[m].pop()

        return res
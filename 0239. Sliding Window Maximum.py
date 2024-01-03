class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hp=[]
        res=[]
        for i in range(k):
            heapq.heappush(hp,[-1*nums[i],i])
        pre=heapq.heappop(hp)
        res.append(-1*pre[0])
        if pre[1]>0:
            heapq.heappush(hp,pre)
        for i in range(k,len(nums)):
            heapq.heappush(hp,[-1*nums[i],i])
            pre=heapq.heappop(hp)
            while i-pre[1]>=k:
                pre=heapq.heappop(hp)
            res.append(-1*pre[0])
            if i-pre[1]<k-1:
                heapq.heappush(hp,pre)
        return res

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap=[]
        res=None
        i=0
        for n in range(k):
            if i<len(arr)-1 and (not heap or heap[0][0]>arr[i]/arr[-1]):
                for j in range(len(arr)-1,i,-1):
                    heapq.heappush(heap,[arr[i]/arr[j],arr[i],arr[j]])
                i+=1
            res=heapq.heappop(heap)[1:]
        return res
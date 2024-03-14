class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr=[]
        for i in range(len(capital)):
            arr.append([profits[i],capital[i]])
        arr.sort(key=lambda x:x[1], reverse=True)
        heap=[]
        for i in range(k):
            while arr and arr[-1][1]<=w:
                heapq.heappush(heap,-1*arr.pop()[0])
            if heap:
                p=-1*heapq.heappop(heap)
                w+=p
        return w
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dic=collections.Counter(arr)
        heapq.heapify(arr)
        while arr:
            c=heapq.heappop(arr)
            if dic[c]<=0:continue
            dic[c]-=1
            if c>=0:d=2*c
            elif c%2:return False
            else:d=c//2
            if d not in dic or dic[d]<=0:
                return False
            dic[d]-=1
        return True

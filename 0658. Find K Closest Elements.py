class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        p=bisect.bisect(arr,x)
        lst=[]
        lst.extend(arr[max(p-k,0):p])
        lst.extend(arr[p:p+k])
        lst.sort(key=lambda y:(abs(y-x),y))
        return sorted(lst[:k])
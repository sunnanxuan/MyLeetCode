class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = []
        for n, f, t in trips:
            bisect.insort(arr, (f, n))
            bisect.insort(arr, (t, -n))
        cur = 0
        for p, n in arr:
            cur += n
            if cur > capacity: return False
        return True

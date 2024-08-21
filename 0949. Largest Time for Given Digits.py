class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        if arr[0]>2:return ""
        p=bisect.bisect_right(arr,2)
        for i in range(p-1,-1,-1):
            h1=arr.pop(i)
            if h1==2:
                if arr[0]>3:
                    bisect.insort(arr,h1)
                    continue
                else:
                    j=bisect.bisect_right(arr,3)
                    h2=arr.pop(j-1)
            else:
                h2=arr.pop()
            if arr[0]>5:
                bisect.insort(arr,h1)
                bisect.insort(arr,h2)
                continue
            p=bisect.bisect_right(arr,5)
            m1=arr.pop(p-1)
            m2=arr.pop()
            return '{}{}:{}{}'.format(h1,h2,m1,m2)
        return ""
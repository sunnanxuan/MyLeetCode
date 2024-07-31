class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left={}
        right={}
        stack_l=[(-1*float('inf'),-1)]
        stack_r=[(-1*float('inf'),len(arr))]
        for i in range(len(arr)):
            while stack_l[-1][0]>=arr[i]:
                stack_l.pop()
            left[i]=i-stack_l[-1][1]
            stack_l.append((arr[i],i))
        for i in range(len(arr)-1,-1,-1):
            while stack_r[-1][0]>arr[i]:
                stack_r.pop()
            right[i]=stack_r[-1][1]-i
            stack_r.append((arr[i],i))
        res=0
        mod=10**9+7
        for i in range(len(arr)):
            res+=(arr[i]*left[i]*right[i])
            res%=mod
        return res
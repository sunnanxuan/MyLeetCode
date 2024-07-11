class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res=float('inf')
        sm=0
        c=0
        stack=[]
        for i in range(len(nums)):
            if not stack and nums[i]<=0:continue
            sm+=nums[i]
            c+=1
            if nums[i]>0:stack.append([nums[i],1])
            elif nums[i]<=0:
                cur=nums[i]
                m=1
                while stack and cur<=0:
                    p,n=stack.pop()
                    cur+=p
                    m+=n
                if cur>0:stack.append([cur,m])
                else:sm=c=0
            if sm>=k:
                while sm-stack[0][0]>=k:
                    p,n=stack.pop(0)
                    sm-=p
                    c-=n
                res=min(res,c)
        return res if res!=float('inf') else -1
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        q=[[[],0,0]]
        for i in range(1,10):
            new=[]
            for nums,sm,j in q:
                if sm+i==n and j+1==k:
                    res.append(nums+[i])
                elif sm+i<n and j+1<k:
                    new.append([nums+[i],sm+i,j+1])
            q.extend(new)
        return res

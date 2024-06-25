class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        merge=list(zip(difficulty,profit))
        merge.sort()
        difficulty.sort()
        pre=0
        maxprofix=[0]*len(profit)
        for i in range(len(profit)):
            pre=max(pre,merge[i][1])
            maxprofix[i]=pre
        res=0
        for w in worker:
            p=bisect.bisect_right(difficulty,w)
            if p>0:
                res+=maxprofix[p-1]
        return res
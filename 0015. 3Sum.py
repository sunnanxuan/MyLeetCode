class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        neg,pos,zeros=[],[],[]
        for num in nums:
            if num>0:pos.append(num)
            elif num==0:zeros.append(num)
            elif num<0:neg.append(num)
        N=set(neg)
        P=set(pos)
        if len(zeros)>=3:
            res.add((0,0,0))
        if len(zeros):
            for nn in N:
                if -1*nn in P:
                    res.add((nn,0,-1*nn))
        for i in range(len(neg)-1):
            for j in range(i+1,len(neg)):
                if -1*(neg[i]+neg[j]) in P:
                    res.add((neg[i],neg[j],-1*(neg[i]+neg[j])))
        for i in range(len(pos)-1):
            for j in range(i+1,len(pos)):
                if -1*(pos[i]+pos[j]) in N:
                    res.add((-1*(pos[i]+pos[j]),pos[i],pos[j]))
        return res

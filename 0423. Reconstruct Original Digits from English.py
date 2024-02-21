class Solution:
    def originalDigits(self, s: str) -> str:
        cases=['z','w','u','o','x','g','s','v','r','i']
        nums={'z':['0','o','r'],'w':['2','t','o'],'o':['1',],'u':['4','r','o'],'x':['6','s','i'],'g':['8','t','i'],'s':['7','v',],'v':['5','i'],'r':['3'],'i':['9']}
        res=[]
        count=collections.Counter(s)
        for c in cases:
            if c in count and count[c]:
                num=nums[c]
                res.extend([num[0]]*count[c])
                for n in num[1:]:
                    count[n]-=count[c]
                count.pop(c)
        res.sort()
        return ''.join(res)
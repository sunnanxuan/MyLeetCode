class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn==0:
            return ['0:00']
        hours=[1,2,4,8]
        minutes=[1,2,4,8,16,32]
        res=[]
        for i in range(min(5,turnedOn+1)):
            j=turnedOn-i
            h=[]
            m=[]
            if i==0:
                h.append('0')
            else:
                for hs in itertools.combinations(hours,i):
                    sm=sum(hs)
                    if sm<12:
                        h.append(str(sm))
            if m==0:
                m.append('0')
            else:
                for ms in itertools.combinations(minutes,j):
                    sm=sum(ms)
                    if sm<60:
                        m.append(str(sm))
            for l in h:
                for r in m:
                    res.append(l+':'+r.zfill(2))
        return res

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound<2:return []
        res=[]
        if x==y==1:
            if bound>=2:res.append(2)
        elif x==1:
            sm=1
            for j in range(int(math.log(bound,y))+1):
                if sm+y**j>bound:break
                res.append(sm+y**j)
        elif y==1:
            sm=1
            for i in range(int(math.log(bound,x))+1):
                if sm+x**i>bound:break
                res.append(sm+x**i)
        else:
            for i in range(int(math.log(bound,x))+1):
                sm=x**i
                for j in range(int(math.log(bound,y))+1):
                    if sm+y**j>bound:break
                    res.append(sm+y**j)
        res=list(set(res))
        return res

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.range=[]
        self.sm=0
        self.rects=sorted(rects)
        for x1,y1,x2,y2 in self.rects:
            self.sm+=(x2-x1+1)*(y2-y1+1)
            self.range.append(self.sm)


    def pick(self) -> List[int]:
        d=randint(0,self.sm)
        p=bisect.bisect_left(self.range,d)
        x1,y1,x2,y2=self.rects[p]
        return [random.randint(x1, x2), random.randint(y1, y2)]
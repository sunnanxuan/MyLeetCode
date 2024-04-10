class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p=[p1,p2,p3,p4]
        dic=collections.defaultdict(int)
        for i in range(4):
            for j in range(i+1,4):
                l=((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)
                dic[l]+=1
        k=sorted(list(dic.keys()))
        if len(k)==2:
            if dic[k[0]]==4 and dic[k[1]]==2:return True
            else:
                return False
        else:
            return False
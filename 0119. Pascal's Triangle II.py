class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        if rowIndex==0:
            return res
        res=[1,1]
        for i in range(2,rowIndex+1):
            new=[1]
            for j in range(1,i):
                new.append(res[j-1]+res[j])
            new.append(1)
            res=new
        return res
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic=collections.defaultdict(dict)
        for i in range(len(equations)):
            m=equations[i][0]
            n=equations[i][1]
            dic[m][n]=values[i]
            dic[n][m]=1/values[i]
            for c in dic[n]:
                if c not in dic[m]:
                    dic[m][c]=dic[n][c]/dic[n][m]
                    dic[c][m]=1/dic[m][c]
            for k in dic[m]:
                if k not in dic[n]:
                    dic[n][k]=dic[m][k]/values[i]
                    dic[k][n]=1/dic[n][k]
            for c in dic[n]:
                for k in dic[m]:
                    if c not in dic[k]:
                        dic[k][c]=dic[k][n]*dic[n][m]*dic[m][c]
                        dic[c][k]=1/dic[k][c]
        res=[]
        for m,n in queries:
            if m not in dic or n not in dic[m]:
                res.append(-1.0)
            else:
                res.append(dic[m][n])
        return res

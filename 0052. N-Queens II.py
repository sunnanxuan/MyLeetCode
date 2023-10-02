class Solution:
    def totalNQueens(self, n: int) -> int:
        res=[0]
        attack=[set(),set(),set()]
        def dfs(i,attack):
            for j in range(n):
                if all(j not in s for s in attack):
                    if i==n-1:
                        res[0]+=1
                    else:
                        l=set()
                        r=set()
                        for k in attack[0]:
                            if k-1>=0:l.add(k-1)
                        if j-1>=0:l.add(j-1)
                        for k in attack[2]:
                            if k+1<n:r.add(k+1)
                        if j+1<n:r.add(j+1)
                        m=attack[1]|{j}

                        dfs(i+1,[l,m,r])
        dfs(0,attack)
        return res[0]
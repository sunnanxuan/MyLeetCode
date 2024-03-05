class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        lst=[]
        for s in strs:
            lst.append([s.count('0'),s.count('1')])
        memo={}
        def count(i,z,o):
            if (i,z,o) in memo:
                return memo[(i,z,o)]
            if i==len(lst):
                return 0
            if z+lst[i][0]<=m and o+lst[i][1]<=n:
                memo[(i,z,o)]=max(1+count(i+1,z+lst[i][0],o+lst[i][1]),count(i+1,z,o))
                return memo[(i,z,o)]
            else:
                memo[(i,z,o)]=count(i+1,z,o)
                return memo[(i,z,o)]
        return count(0,0,0)
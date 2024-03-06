class Solution:
    def magicalString(self, n: int) -> int:
        if n==1:
            return 1
        s='122'
        m=2
        cur='1'
        l=3
        while l<n:
            s+=cur*int(s[m])
            l+=int(s[m])
            m+=1
            if cur=='1':cur='2'
            elif cur=='2':cur='1'
        return s[:n].count('1')
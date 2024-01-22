class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def additive(m,n,s):
            if (m=='0' or m[0]!='0') and (n=='0' or n[0]!='0') and str(int(m)+int(n))==s[:len(str(int(m)+int(n)))]:
                if len(s)==len(str(int(m)+int(n))):
                    return True
                else:
                    return additive(n,str(int(m)+int(n)),s[len(str(int(m)+int(n))):])
            else:
                return False

        #return any([additive(num[:i],num[i:j],num[j:]) for i in range(1,len(num)-1) for j in range(i+1,len(num))])

        for i in range(1,len(num)-1):
            for j in range(i+1,len(num)):
                if additive(num[:i],num[i:j],num[j:])==True:
                    return True
        return False
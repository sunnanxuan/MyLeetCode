class Solution:
    def numDecodings(self, s: str) -> int:
        mod=10**9+7
        if s[0]=='0':return 0
        if s[0].isdigit():sec=1
        else:sec=9
        fir=1
        for i in range(1,len(s)):
            if s[i]=='0':
                if s[i-1]=='*':cur=fir*2
                elif s[i-1] not in '12':return 0
                else:cur=fir
            elif s[i].isdigit():
                if s[i-1]=='1':cur=fir+sec
                elif s[i-1]=='2':
                    if s[i] in '123456':cur=fir+sec
                    else:cur=sec
                elif s[i-1]=='*':
                    if s[i] in '123456':cur=fir*2+sec
                    else:cur=fir+sec
                else:cur=sec
            else:
                if s[i-1]=='1':cur=fir*9+sec*9
                elif s[i-1]=='2':cur=fir*6+sec*9
                elif s[i-1]=='*':cur=fir*15+sec*9
                else:cur=sec*9
            cur%=mod
            fir=sec
            sec=cur
        return sec

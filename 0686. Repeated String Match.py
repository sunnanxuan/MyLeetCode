class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if set(b)-set(a):return -1
        elif not b:return 0
        elif b in a:return 1
        else:
            c=0
            s=a*2
            while c<=len(b)//len(a)+1:
                if b in s:return 2+c
                else:
                    c+=1
                    s+=a
            return -1
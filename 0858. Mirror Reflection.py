class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        cur=p
        d=1
        while True:
            if cur%q==0:
                if cur//q%2==d:return 1
                else:return 2
            else:
                if cur//q%2==0:
                    if d==0:d=1
                    else:d=0
                n=cur%q
                cur=p-q+n
                if cur%q==0 and cur//q%2==d:return 0
                else:
                    if cur//q%2==0:
                        if d==0:d=1
                        else:d=0
                    n=cur%q
                    cur=p-q+n

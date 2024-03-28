class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack=[]
        switch=False
        for c in str(n)[::-1]:
            if not switch and stack and stack[-1]>c:
                p=bisect.bisect_right(stack,c)
                m=stack.pop(p)
                stack.append(c)
                stack.sort(reverse=True)
                stack.append(m)
                switch=True
            elif switch:
                stack.append(c)
            else:
                bisect.insort(stack,c)
        new=int(''.join(stack[::-1]))
        return (new==n or new>=2**31) and -1 or new
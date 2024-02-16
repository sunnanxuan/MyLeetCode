class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        r=0
        stack=[]
        for n in num:
            while r<k and stack and stack[-1]>n:
                stack.pop()
                r+=1
            stack.append(n)
        while r<k:
            stack.pop()
            r+=1
        return ''.join(stack).lstrip('0') or '0'
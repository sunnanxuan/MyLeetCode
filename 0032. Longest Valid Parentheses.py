class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        res=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                if '(' not in stack:
                    res=max(res,len(stack)*2)
                    stack=[]
                else:
                    j=len(stack)-1
                    while stack[j]=='*':
                        j-=1
                    stack.pop(j)
                    stack.append('*')
        l=0
        for i in range(len(stack)):
            if stack[i]=="*":
                l+=2
            else:
                res=max(res,l)
                l=0
        res=max(res,l)
        return res
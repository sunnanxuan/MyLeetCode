class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        left = right = 0
        i = 0
        stack = []
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
                left += 1
            if s[i] == ')':
                stack.append(')')
                right += 1
            if left == right:
                stack.pop()
                stack.pop(0)
                res.extend(stack)
                stack = []
            i += 1
        return ''.join(res)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [""]
        for c in s:
            if c.isdigit():
                if stack[-1].isdigit():
                    stack[-1] += c
                else:
                    stack.append(c)
            elif c == '[':
                stack.append('')
            elif c.islower():
                stack[-1] += c
            elif c == ']':
                m = stack.pop()
                n = stack.pop()
                mn = int(n) * m
                if stack[-1].isdigit():
                    stack.append(mn)
                else:
                    stack[-1] += mn
        return ''.join(stack)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for k in s:
            if k in '([{':
                stack.append(k)
            elif k == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif k == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif k == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False


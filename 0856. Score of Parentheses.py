class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                cur = 0
                while stack:
                    m = stack.pop()
                    if m == '(':
                        if cur == 0:
                            stack.append(1)
                        else:
                            stack.append(cur * 2)
                        break
                    else:
                        cur += m
        return sum(stack)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.isdigit() or c[1:].isdigit():
                stack.append(int(c))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if c == '+':
                    m = n1 + n2
                elif c == '-':
                    m = n1 - n2
                elif c == '*':
                    m = n1 * n2
                elif c == '/':
                    if n1 * n2 >= 0:
                        m = n1 // n2
                    else:
                        m = -1 * (abs(n1) // abs(n2))
                stack.append(m)
        res = stack.pop()
        return res


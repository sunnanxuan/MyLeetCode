class Solution:
    def calculate(self, s):
        def operation(m1, m2, op):
            if op == '+':
                return m1 + m2
            elif op == '-':
                return m1 - m2

        stack = []
        i = 0
        cur = None
        while i < len(s):
            if s[i].isdigit():
                j = i + 1
                num = [s[i]]
                while j < len(s) and s[j].isdigit():
                    num.append(s[j])
                    j += 1
                cur = int(''.join(num))
                i = j

            elif s[i] == '(' or s[i] == '+' or s[i] == '-':
                stack.append(s[i])
                i += 1
            elif s[i] == ')':
                i += 1
                cur = stack.pop()
                stack.pop()
            else:
                i += 1
            if cur != None:
                if not stack or stack[-1] == '(':
                    stack.append(cur)
                else:
                    op = stack.pop()
                    if stack and stack[-1] != '(':
                        m1 = stack.pop()
                        n = operation(m1, cur, op)
                    else:
                        if op == '+':
                            n = cur
                        elif op == '-':
                            n = -1 * cur
                    stack.append(n)
                cur = None
        return stack[-1]

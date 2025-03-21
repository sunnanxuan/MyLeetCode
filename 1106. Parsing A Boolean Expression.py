class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def boolean(op, lst):
            if op == '&':
                return all(lst)
            elif op == '|':
                return any(lst)
            elif op == '!':
                return not lst[0]

        op = []
        stack = []
        for c in expression:
            if c == ')':
                lst = []
                cur = stack.pop()
                while cur != '(':
                    lst.append(cur)
                    cur = stack.pop()
                stack.append(boolean(op.pop(), lst))
            elif c == 't':
                stack.append(True)
            elif c == 'f':
                stack.append(False)
            elif c == '(':
                stack.append(c)
            elif c == ',':
                continue
            else:
                op.append(c)

        return stack[0]


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        d = ''
        dot = ''
        for c in path + '/':
            if c == '/':
                print()
                if len(dot) == 2:
                    if len(stack) >= 2:
                        stack.pop()
                        stack.pop()
                elif len(dot) >= 3:
                    stack.append(dot)
                dot = ''
                if d:
                    stack.append(d)
                    d = ''
                if not stack or stack[-1] != '/':
                    stack.append('/')
            elif c == '.' and not d:
                if not stack:
                    stack.append('/')
                dot += c

            else:
                if dot:
                    d = dot + c
                    dot = ''
                else:
                    d += c
        if len(stack) >= 2:
            stack.pop()

        return ''.join(stack)

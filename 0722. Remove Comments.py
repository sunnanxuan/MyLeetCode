class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        stack = []
        block = [None]

        def remove(s):
            if block[0] != None:
                if '*/' in s:
                    while len(stack) > block[0]:
                        pre = stack.pop()
                    p = s.index('*/')
                    tail = s[p + 2:]
                    block[0] = None
                    return remove(pre + tail)
                elif '//' in s:
                    p = s.index('//')
                    return s[:p]
                else:
                    return s
            else:
                p1 = p2 = -1
                if '//' in s: p1 = s.index('//')
                if '/*' in s: p2 = s.index('/*')
                if p1 == p2 == -1:
                    return s
                elif (p1 >= 0 and p2 == -1) or (p1 >= 0 and p1 < p2):
                    return s[:p1]
                else:
                    block[0] = len(stack)
                    stack.append(s[:p2])
                    if not s[p2 + 2:]:
                        stack.append('')
                        return ''
                    else:
                        return remove(s[p2 + 2:])

        for s in source:
            c = remove(s)
            if len(c) > 0: stack.append(c)
        if block[0] != None:
            cur = stack.pop(block[0] + 1)
            stack[block[0]] += ('/*' + cur)
        return stack


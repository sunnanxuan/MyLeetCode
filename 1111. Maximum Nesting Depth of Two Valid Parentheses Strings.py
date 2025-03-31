class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        nest = []
        deep = []
        stack = []
        p = h = 0
        for c in seq:
            if c == '(':
                p += 1
                h = max(h, p)
            elif c == ')':
                p -= 1
            stack.append(c)
            if p == 0:
                deep.append(h)
                nest.append(''.join(stack))
                stack = []
        d = max(deep) // 2
        res = []
        for s in nest:
            p = 0
            for c in s:
                if c == '(':
                    p += 1
                    if p <= d:
                        res.append(0)
                    else:
                        res.append(1)
                else:
                    p -= 1
                    if p <= d - 1:
                        res.append(0)
                    else:
                        res.append(1)
        return res





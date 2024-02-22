class Solution:
    def countSegments(self, s: str) -> int:
        n = 0
        pre = False
        for c in s:
            if c != ' ' and not pre:
                n += 1
                pre = True
            elif c == ' ':
                pre = False
        return n

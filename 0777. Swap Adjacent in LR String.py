class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        dic_s = collections.Counter(start)
        dic_e = collections.Counter(end)
        if any([dic_s[k] != dic_e[k] for k in dic_s]): return False
        s = [c for c in start]
        i = 0
        while i < len(s):
            if s[i] == end[i]:
                i += 1
            else:
                if end[i] == 'R': return False
                if s[i] == 'L':
                    return False
                elif s[i] == 'R':
                    if end[i] == 'L': return False
                    j = i
                    while s[j] != 'X':
                        if s[j] == 'L':
                            return False
                        else:
                            j += 1
                    s.pop(j)
                    s.insert(i, 'X')
                    i += 1

                elif end[i] == 'L':
                    j = i
                    while s[j] != 'L':
                        if s[j] == 'R':
                            return False
                        else:
                            j += 1
                    s.pop(j)
                    s.insert(i, 'L')
                    i += 1
                elif s[i] == 'X':
                    j = i
                    while s[j] != 'L':
                        if s[j] == 'R':
                            return False
                        else:
                            j += 1
                    s.pop(j)
                    s.insert(i, 'L')
                    i += 1
        return True
